# Generated by Django 4.1.2 on 2022-10-15 00:12

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_alter_ong_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ong',
            name='password',
            field=models.CharField(max_length=100, validators=[core.models.validate_password]),
        ),
    ]
