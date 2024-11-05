# Generated by Django 5.1.1 on 2024-10-03 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appportfolio', '0003_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulacion', models.CharField(blank=True, max_length=25, null=True, verbose_name='Titulo')),
                ('fechaInicio', models.DateField(blank=True, null=True, verbose_name='Fecha Inicio')),
                ('fechaFin', models.DateField(blank=True, null=True, verbose_name='Fecha Final')),
                ('notaMedia', models.IntegerField(blank=True, null=True, verbose_name='Nota Media')),
                ('lugarEstudio', models.CharField(blank=True, max_length=25, null=True, verbose_name='Lugar Estudio')),
                ('nombreLugar', models.CharField(blank=True, max_length=25, null=True, verbose_name='Nombre Lugar')),
                ('ciudad', models.CharField(blank=True, max_length=25, null=True, verbose_name='Ciudad')),
                ('presencial', models.BooleanField(blank=True, null=True, verbose_name='Presencial')),
                ('observaciones', models.TextField(blank=True, null=True, verbose_name='Observaciones')),
            ],
            options={
                'verbose_name': 'Estudio',
                'verbose_name_plural': 'Estudios',
                'ordering': ['titulacion'],
            },
        ),
    ]
