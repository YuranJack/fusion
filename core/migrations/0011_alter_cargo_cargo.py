# Generated by Django 4.1 on 2022-08-31 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_funcionario_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargo',
            name='cargo',
            field=models.CharField(max_length=30, verbose_name='Cargo'),
        ),
    ]