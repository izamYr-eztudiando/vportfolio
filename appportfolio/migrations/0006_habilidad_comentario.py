# Generated by Django 5.1.1 on 2024-10-10 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appportfolio', '0005_experiencia_alter_estudio_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='habilidad',
            name='comentario',
            field=models.TextField(blank=True, max_length=255, null=True, verbose_name='Comentario'),
        ),
    ]