# Generated by Django 3.0.7 on 2020-06-15 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calcularConf', '0002_auto_20200615_1333'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empresa',
            old_name='indiceDeConf',
            new_name='indiceDeConfFloat',
        ),
        migrations.AddField(
            model_name='empresa',
            name='indiceDeConfInt',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
