# Generated by Django 3.2 on 2024-10-31 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appportfolio', '0009_auto_20241031_1030'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagen',
            options={'ordering': ['id'], 'verbose_name': 'Image', 'verbose_name_plural': 'Images'},
        ),
    ]