# Generated by Django 5.0.2 on 2024-02-08 04:43

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Refugio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(blank=True, max_length=144)),
                ('nombre', models.CharField(max_length=144)),
                ('descipcion', models.TextField(blank=True, null=True)),
                ('ciudad', models.CharField(default='Quito', max_length=144)),
            ],
        ),
        migrations.CreateModel(
            name='Perro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=144)),
                ('descipcion', models.TextField(blank=True, null=True)),
                ('ficha_perro', models.FileField(upload_to='uploads/')),
                ('fecha_nacimiento', models.DateTimeField(blank=True)),
                ('fecha_actualizacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('refugio_actual', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='perros', to='lider.refugio')),
            ],
        ),
    ]
