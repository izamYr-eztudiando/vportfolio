# Generated by Django 4.1.5 on 2024-11-29 12:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appportfolio', '0014_valoracion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(blank=True, max_length=25, null=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Estado',
                'verbose_name_plural': 'Estados',
                'ordering': ['estado'],
            },
        ),
        migrations.CreateModel(
            name='Tareas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tarea', models.CharField(blank=True, max_length=25, null=True, verbose_name='Tarea')),
                ('fecha', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha')),
                ('estado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tareas_estado', to='appportfolio.estado')),
            ],
            options={
                'verbose_name': 'Tarea',
                'verbose_name_plural': 'Tareas',
                'ordering': ['tarea'],
            },
        ),
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField(verbose_name='Contenido del mensaje')),
                ('fecha_envio', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de envío')),
                ('leido', models.BooleanField(default=False, verbose_name='Leído')),
                ('destinatario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensajes_recibidos', to=settings.AUTH_USER_MODEL)),
                ('remitente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensajes_enviados', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['fecha_envio'],
            },
        ),
    ]
