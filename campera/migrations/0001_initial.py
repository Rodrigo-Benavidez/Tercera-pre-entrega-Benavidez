# Generated by Django 4.2.6 on 2023-11-14 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talle', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=250)),
                ('fecha_creación', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Estilo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abrigo', models.CharField(max_length=30)),
                ('rompeviento', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=250)),
                ('fecha_creación', models.DateField()),
            ],
        ),
    ]
