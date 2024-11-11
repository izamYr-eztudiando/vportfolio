from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from django.http  import HttpResponse
from appportfolio.models import *

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger	#paginacion
from django.contrib.auth import authenticate, get_user_model, login,logout  #todas son por defecto
from django.contrib.auth.decorators import login_required
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout
from django.views.decorators.csrf import csrf_protect

from django.contrib.auth.models import User
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

#email
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib import messages

#pdf's
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Create your views here.

DEBUG = True

'''
def home(request):
    cadena="<center>Hola Mundo</center><br><br><hr><img src='data:image/jpeg;base64,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'>"
    return HttpResponse(cadena)
'''

# Este home es cuando el usuario no esta autenticado
def home_not_authenticated(request):
    global DEBUG
    print("hola estoy en home "+str(DEBUG))
    nombreProyecto = 'PORTFOLIO'
    fechaCreacion = '23/09/2024'
    usuario = 'prueba'
    context = {'nombreProyecto': nombreProyecto, 'fechaCreacion': fechaCreacion, 'usuario':usuario} 
    return render(request, 'home.html', context=context)

# Este home es cuando el usuario esta autenticado
def home(request):
    global DEBUG
    print("hola estoy en home "+str(DEBUG))
    nombreProyecto = 'PORTFOLIO'
    fechaCreacion = '23/09/2024'
    actual = request.user
    numconectados = 0
    dato = ""
    
    # ip externa o pública
    lista = "0123456789."
    ip=""
    
    try:
        dato = urllib.request.urlopen('https://www.wikipedia.org').headers['X-Client-IP']
        print("IP PUBLICA= " +str(dato) )
    except:
        print("Error en la Libreria de la IP")
        dato = ""
    finally:
        print("USUARIO ACTUAL= [" +str(actual)+"]" )

    for x in str(dato):
        if x in lista:
            ip += x

    if str(actual) == "AnonymousUser":
        request.session['anonimo'] = 'anonimo'
        print("IP ANONIMA= " +str(ip) )
    
    usuario = 'prueba'

    #imagen usuario

    idusuario=0
    idusuario=actual.id 
    request.session['idusuario']=idusuario
    print("idusuario="+str(idusuario))
    entrevistador=Entrevistador.objects.get(user=idusuario)
    idEntrevistador=entrevistador.id
    print("idEntrevistador="+str(idEntrevistador))
    print("FOTO="+str(entrevistador.avatar))
    fotoperfil = settings.MEDIA_URL + str(entrevistador.avatar) if entrevistador.avatar else settings.MEDIA_URL +"MONEDA3.jpg"
    print("avatar=" + str(fotoperfil))
    context = {'fotoperfil':fotoperfil}
    #return redirect('home')  
    context = {'nombreProyecto':nombreProyecto, 'fechaCreacion':fechaCreacion, 'usuario':usuario, 'fotoperfil':fotoperfil}
    #context = {'nombreProyecto':nombreProyecto, 'fechaCreacion':fechaCreacion, 'usuario':usuario}
    return render(request, 'home.html', context=context)

def navbar(request):
    idusuario = 0
    actual = request.user
    idusuario = actual.id
    request.session['idusuario']=idusuario
    entrevistador=Entrevistador.objects.get(user=idusuario)
    fotoperfil = settings.MEDIA_URL + str(entrevistador.avatar) if entrevistador.avatar else settings.MEDIA_URL + 'MONEDA3.jpg'
    context = {'fotoperfil':fotoperfil}
    return render(request, 'navbar.html', context=context)
    
def sobremi(request):
    print("hola estoy en sobremi")
    nombre = 'Isamir'
    edad = 59
    telefono = '674834567'
    cargo = 'Esclavo de su destino'
    listaCategorias = Categoria.objects.all().order_by('-id')
    for r in listaCategorias:
        print(str(r.nombre_categoria))
    context = {'nombre':nombre, 'edad':edad, 'telefono':telefono, 'cargo':cargo, 'listaCategorias':listaCategorias}
    return render(request, 'sobremi.html', context=context)
    
def habilidades(request):
    print("hola estoy en habilidades")
    #select * from Habilidades order by habilidad
    #habilidades es un objeto de tipo queryset
    lista_habilidades = Habilidad.objects.all().order_by('habilidad')
    numregistros = 0
    for r in lista_habilidades:
        numregistros = numregistros + 1
    page = request.GET.get('page')
    paginator = Paginator(lista_habilidades, 5)
    if page == None:
        print(" page recibe fuera de get o post NONE=" + str(page))
        page = paginator.num_pages
        request.session["pagina"] = page
    else:
        print(" page recibe esle del none de geo o post=" + str(page))
        request.session["pagina"] = page

    if request.method == 'GET':
        pagina = request.session["pagina"]
        print(" page recibe en GET=" + str(pagina))
    if request.method == 'POST':
        pagina = request.session["pagina"]
        print(" page recibe en POST=" + str(pagina))

    # condición muy importante para saber si existe la variable en la sesión
    if "pagina" in request.session:
        page = request.session["pagina"]
        print(" page recibe de sesion=" + str(page))

    try:
        lista_habilidades = paginator.get_page(page)
    except PageNotAnInteger:
        lista_habilidades = paginator.page(1)
    except EmptyPage:
        lista_habilidades = paginator.page(paginator.num_pages)

    context = {'lista_habilidades': lista_habilidades, 'numregistros':numregistros}
    return render(request, 'habilidades.html', context=context)

def agregarHabilidad(request):
    print("AGREGAR")
    if request.method == 'POST':
        habilidad = request.POST.get('habilidad')
        nivel = request.POST.get('nivel')
        comentario = request.POST.get('comentario')
        habilidad = Habilidad(habilidad=habilidad, nivel=nivel, comentario=comentario)
        habilidad.save()
        return redirect('habilidades')
    return render(request, 'agregar_habilidad.html')

def ver_habilidad(request,id):
    expe_id=id
    habilidad = Habilidad.objects.get(id=expe_id)
    context = {'habilidad': habilidad}
    return render(request, 'ver_habilidad.html', context=context)

def modificarHabilidad(request, id):
    habilidad = Habilidad.objects.get(id=id)
    if request.method == 'POST':
        habilidad.habilidad = request.POST.get('habilidad')
        habilidad.nivel = request.POST.get('nivel')
        habilidad.comentario = request.POST.get('comentario')
        habilidad.save()
        return redirect('habilidades')
    return render(request, 'editar_habilidad.html', {'habilidad':habilidad})

def eliminarHabilidad(request, pk):
    print("ELIMINAR")
    expe_id = pk
    habilidad = Habilidad.objects.get(id=expe_id)
    if request.method == 'POST':
        habilidad.delete()
        return redirect('home')
    return render(request, 'eliminar_habilidad.html', {'habilidad': habilidad})

def categorias(request):
    print("hola estoy en categorias")
    #El metodo Alfonso
    lista_categorias = Categoria.objects.all()  # select * from Experiencias;
    numregistros = 0
    for r in lista_categorias:
        numregistros = numregistros + 1
    page = request.GET.get('page')
    # 2 registros por página
    paginator = Paginator(lista_categorias, 5)
    if page == None:
        print(" page recibe fuera de get o post NONE=" + str(page))
        page = paginator.num_pages
        request.session["pagina"] = page
    else:
        print(" page recibe esle del none de geo o post=" + str(page))
        request.session["pagina"] = page

    if request.method == 'GET':
        pagina = request.session["pagina"]
        print(" page recibe en GET=" + str(pagina))
    if request.method == 'POST':
        pagina = request.session["pagina"]
        print(" page recibe en POST=" + str(pagina))

    #condición muy importante para saber si existe la variable en la sesión
    if "pagina" in request.session:
        page = request.session["pagina"]
        print(" page recibe de sesion=" + str(page))

    try:
        lista_categorias = paginator.get_page(page)
    except PageNotAnInteger:
        lista_categorias = paginator.page(1)
    except EmptyPage:
        lista_categorias = paginator.page(paginator.num_pages)

    context = {'lista_categorias': lista_categorias, 'numregistros':numregistros}
    return render(request, 'categorias.html', context=context)

def estudios(request):
    print("hola estoy en estudios")
    # El metodo Alfonso
    lista_estudios = Estudio.objects.all()  # select * from Experiencias;
    numregistros = 0
    for r in lista_estudios:
        numregistros = numregistros + 1
    page = request.GET.get('page')
    # 2 registros por página
    paginator = Paginator(lista_estudios, 3)
    if page == None:
        print(" page recibe fuera de get o post NONE=" + str(page))
        page = paginator.num_pages
        request.session["pagina"] = page
    else:
        print(" page recibe esle del none de geo o post=" + str(page))
        request.session["pagina"] = page

    if request.method == 'GET':
        pagina = request.session["pagina"]
        print(" page recibe en GET=" + str(pagina))
    if request.method == 'POST':
        pagina = request.session["pagina"]
        print(" page recibe en POST=" + str(pagina))

    # condición muy importante para saber si existe la variable en la sesión
    if "pagina" in request.session:
        page = request.session["pagina"]
        print(" page recibe de sesion=" + str(page))

    try:
        lista_estudios = paginator.get_page(page)
    except PageNotAnInteger:
        lista_estudios = paginator.page(1)
    except EmptyPage:
        lista_estudios = paginator.page(paginator.num_pages)

    context = {'lista_estudios': lista_estudios, 'numregistros':numregistros}
    return render(request, 'estudios.html', context=context)

def experiencias(request):
    print("hola estoy en experiencias")
    lista_experiencias = Experiencia.objects.all().order_by('id')
    numregistros = 0
    for r in lista_experiencias:
        numregistros = numregistros + 1
    page = request.GET.get('page')
    paginator = Paginator(lista_experiencias, 2)
    if page == None:
        print(" page recibe fuera de get o post NONE=" + str(page))
        page = paginator.num_pages
        request.session["pagina"] = page
    else:
        print(" page recibe esle del none de geo o post=" + str(page))
        request.session["pagina"] = page

    if request.method == 'GET':
        pagina = request.session["pagina"]
        print(" page recibe en GET=" + str(pagina))
    if request.method == 'POST':
        pagina = request.session["pagina"]
        print(" page recibe en POST=" + str(pagina))

    # condición muy importante para saber si existe la variable en la sesión
    if "pagina" in request.session:
        page = request.session["pagina"]
        print(" page recibe de sesion=" + str(page))

    try:
        lista_experiencias = paginator.get_page(page)
    except PageNotAnInteger:
        lista_experiencias = paginator.page(1)
    except EmptyPage:
        lista_experiencias = paginator.page(paginator.num_pages)

    context = {'lista_experiencias': lista_experiencias, 'numregistros': numregistros}
    return render(request, 'experiencias.html', context=context)
def ver_experiencia(request,id):
    expe_id=id
    experiencia = Experiencia.objects.get(id=expe_id)
    context = {'experiencia': experiencia}
    return render(request, 'ver_experiencia.html', context=context)

def eliminarExperiencia(request, pk):
    print("ELIMINAR")
    expe_id = pk
    experiencia = Experiencia.objects.get(id=expe_id)
    if request.method == 'POST':
        experiencia.delete()
        return redirect('home')
    return render(request, 'eliminar_experiencia.html', {'experiencia': experiencia})

def modificarExperiencia(request, pk):
    print("MODIFICAR")
    expe_id = pk
    experiencia = Experiencia.objects.get(id=expe_id)
    if request.method == 'POST':
        experiencia.save()
        return redirect('home')
    return render(request, 'modificar_experiencia.html', {'experiencia': experiencia})

def login_view(request):
    print("login_view")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            actual=request.user   #usuario actual
            idusuario=0
            idusuario=actual.id 
            request.session['idusuario']=idusuario
            print("idusuario="+str(idusuario))
            entrevistador=Entrevistador.objects.get(user=idusuario)
            idEntrevistador=entrevistador.id
            print("idEntrevistador="+str(idEntrevistador))
            print("FOTO="+str(entrevistador.avatar))
            fotoperfil = settings.MEDIA_URL + str(entrevistador.avatar) if entrevistador.avatar else settings.MEDIA_URL +"MONEDA3.jpg"
            print("avatar=" + str(fotoperfil))
            context = {'fotoperfil':fotoperfil}
            return render(request, 'home.html', context=context)
            #return redirect('home')  
        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})
    return render(request, 'Login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return redirect('login') #Redirigir a la página de inicio de sesión
    return render(request, 'register.html')

#Cerrar sesion
def cerrar(request):
    username = request.user.username
    password = request.user.password
    idusuario = request.user.id
    print("logout.............. " + username + "clave = " + str(password) + "id = " + str(idusuario))
    user = authenticate(request, username=username, password=password)
    # desconectar al usuario
    logout(request)
    return redirect('/')

def subirImagen(request):
    print("Subiendo Imagen")
    # idUsuario = request.session['idusuario']
    if request.method == 'POST':
        imagenes = request.FILES.getlist('imagenes')
        for imagen in imagenes:
            if imagen.name.endswith(('.jpg', '.jpeg', '.png', '.gif','.jfif')):
                print("Imagen: " + imagen.name)
                img = Imagen()
                img.imagen = imagen
                img.save()
        return redirect('subirImagen')
    imagenes = Imagen.objects.all()
    return render(request, 'subirImagen.html', {'imagenes': imagenes})

def editarImagen(request, imagen_id):
    imagen = get_object_or_404(Imagen, id = imagen_id)

    if request.method == 'POST' and request.FILES.get('nueva_imagen'):
        imagen.imagen = request.FILES['nueva_imagen']
        imagen.save()
        return redirect('subirImagen')
    
    return redirect('subirImagen')
    
def eliminarImagen(request, imagen_id):
    imagen = get_object_or_404(Imagen, id = imagen_id)
    if request.method == 'POST':
        imagen.delete()
        return redirect('subirImagen') #Redirige a la galeria de imagenes
    
    return redirect('subirImagen')

def subirVideo(request):
    print("Subiendo Video")
    if request.method == 'POST' and request.FILES['videos']:
        videos = request.FILES.getlist('videos')

        for video in videos:
            if video.name.endswith(('.mp4', '.avi', '.mkv', '.mov', '.mp3')):
                v=Video()
                v.video = video
                v.save()
        return redirect('subirVideo')
    
    videos = Video.objects.all()
    return render(request, 'subirVideo.html', {'videos': videos})

def editarVideo(request, video_id):
    video = get_object_or_404(Video, id = video_id)

    if request.method == 'POST' and request.FILES.get('nuevo_video'):
        video.video = request.FILES['nuevo_video'] #Se agarra el archivo subido por el usuario a través del formulario por el name="nuevo_video"
        video.save()
        return redirect('subirVideo')
    
    return redirect('subirVideo')

def eliminarVideo(request, video_id):
    video = get_object_or_404(Video, id = video_id)

    if request.method == 'POST':
        video.delete()
        return redirect('subirVideo')
    
    return redirect('subirVideo')

def contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get("nombre")
        email = request.POST.get("email")
        asunto = request.POST.get("asunto")
        mensaje = request.POST.get("mensaje")

        context = {'nombre':nombre, 'email':email, 'asunto':asunto, 'mensaje':mensaje}
        template = render_to_string('email_template.html', context=context)

        email = EmailMessage(asunto, template,
        settings.EMAIL_HOST_USER, ['isamir.bb8@gmail.com'])

        email.fail_silently = False #que no marque error en gmail
        email.send()

        messages.success(request, 'Su mensaje ha sido enviado exitosamente')
        return redirect('home')
    
    return render(request, 'correo.html')

def listar_entrevistadores(request):
    entrevistadores = Entrevistador.objects.all()
    return render(request, 'listar_entrevistadores.html', {'entrevistadores': entrevistadores})

def generar_pdf(request, entrevistador_id):
    entrevistador = Entrevistador.objects.get(id=entrevistador_id)

    # Crear una respuesta HTTP con contenido tipo PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="entrevistador_{entrevistador.id}.pdf"'

    # Crear el objeto canvas de ReportLab
    p = canvas.Canvas(response, pagesize=letter)
    
    # Configuración del título
    p.setFont("Helvetica-Bold", 16)
    p.setFillColor(colors.darkblue)
    p.drawCentredString(300, 770, "Reporte de Entrevistador")

    # Volver al tamaño de fuente normal
    p.setFont("Helvetica", 12)
    p.setFillColor(colors.black)

    #Datos del entrevistador
    p.drawString(100, 720, f"ID: {entrevistador.id}")
    p.drawString(100, 700, f"Empresa: {entrevistador.empresa or 'N/A'}")
    p.drawString(100, 680, f"Fecha de Entrevista: {entrevistador.fecha_entrevista or 'N/A'}")
    p.drawString(100, 660, f"Conectado: {'Si' if entrevistador.conectado else 'No'}")
    p.drawString(100, 640, f"Seleccionado: {'Si' if entrevistador.seleccionado else 'No'}")
    p.drawString(100, 620, f"Usuario: {entrevistador.user.username if entrevistador.user else 'N/A'}")

    # Añadir avatar si existe
    if entrevistador.avatar:
        avatar_path = entrevistador.avatar.path
        p.drawImage(avatar_path, 100, 500, width = 100, height = 100)

    # Guardar el PDF
    p.showPage()
    p.save()

    return response
    
def subirCurriculum(request):
    print("Subiendo Curriculum")
    if request.method == 'POST':
        curriculums = request.FILES.getlist('curriculums')
        for curriculum in curriculums:
            if curriculum.name.endswith(('.pdf', '.PDF')):
                c=Curriculum()
                c.curriculum = curriculums
                c.save()
        return redirect('subirCurriculum')
    
    curriculum = Curriculum.objects.all()
    return render(request, 'subirCurriculum.html', {'curriculum': curriculum})

def editarCurriculum(request, curriculum_id):
    curriculum = get_object_or_404(Curriculum, id = curriculum_id)

    if request.method == 'POST' and request.FILES.get('nuevo_curriculum'):
        curriculum.curriculum = request.FILES['nuevo_curriculum'] #Se agarra el archivo subido por el usuario a través del formulario por el name="nuevo_curriculum"
        curriculum.save()
        return redirect('subirCurriculum')
    
    return redirect('subirCurriculum')
    
def eliminarCurriculum(request, curriculum_id):
    curriculum = get_object_or_404(Curriculum, id = curriculum_id)
    if request.method == 'POST':
        curriculum.delete()
        return redirect('subirCurriculum') #Redirige a la galeria de curriculum
    
    return redirect('subirCurriculum')