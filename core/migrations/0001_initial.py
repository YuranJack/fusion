# Generated by Django 4.1 on 2022-08-31 20:22

from django.db import migrations, models
import django.db.models.deletion
import pictures.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Data de criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualizado')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('cargo', models.CharField(max_length=20, verbose_name='Cargo')),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargos',
            },
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Data de criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualizado')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('servico', models.CharField(max_length=100, verbose_name='Serviço')),
                ('descricao', models.TextField(max_length=200, verbose_name='Descrição')),
                ('icone', models.CharField(choices=[('lni-cog', 'Engrenagem'), ('lni-stats-up', 'Gráfico'), ('lni-users', 'Usuários'), ('lni-layers', 'Design'), ('lni-mobile', 'Mobile'), ('lni-rocket', 'Foguete')], max_length=12, verbose_name='Icone')),
            ],
            options={
                'verbose_name': 'Serviço',
                'verbose_name_plural': 'Serviços',
            },
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Data de criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualizado')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('bio', models.TextField(max_length=200, verbose_name='Bio')),
                ('imagem', pictures.models.PictureField(aspect_ratios=[None], breakpoints={'l': 1200, 'm': 992, 's': 768, 'xl': 1400, 'xs': 576}, container_width=1200, file_types=['PNG', 'JPEG'], grid_columns=12, pixel_densities=[1, 2], upload_to='equipe', verbose_name='Imagem')),
                ('facebook', models.CharField(default='#', max_length=200, verbose_name='Facebook')),
                ('twitter', models.CharField(default='#', max_length=200, verbose_name='Twitter')),
                ('instagram', models.CharField(default='#', max_length=200, verbose_name='Instagram')),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cargo', verbose_name='cargo')),
            ],
            options={
                'verbose_name': 'Funcionário',
                'verbose_name_plural': 'Funcionários',
            },
        ),
    ]