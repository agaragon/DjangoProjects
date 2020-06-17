# Generated by Django 2.2.2 on 2020-06-17 19:59

import calcularConf.static.rotinas.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calcularConf', '0002_auto_20200617_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infodasempresas',
            name='arquivo',
            field=models.FileField(null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['json']), calcularConf.static.rotinas.validators.file_size]),
        ),
    ]
