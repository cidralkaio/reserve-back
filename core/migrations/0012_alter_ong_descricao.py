# Generated by Django 4.1.2 on 2022-10-14 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_remove_ong_uf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ong',
            name='descricao',
            field=models.CharField(default='sem descrição', max_length=1000, null=True),
        ),
    ]
