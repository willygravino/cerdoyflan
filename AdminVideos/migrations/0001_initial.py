# Generated by Django 4.1.7 on 2023-03-29 12:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_video', models.CharField(max_length=30)),
                ('url_video', models.CharField(max_length=80)),
                ('descripcion_video', models.CharField(max_length=300)),
                ('quienes_aparecen', models.CharField(max_length=120, verbose_name='Ingrese el nombre y apellido de quienes participan en el video, separados por coma')),
                ('image', models.ImageField(blank=True, null=True, upload_to='videos/')),
                ('fecha_video', models.DateTimeField()),
                ('propietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='propietario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_completo', models.CharField(max_length=80)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatares')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensaje', models.TextField(max_length=1000)),
                ('email', models.EmailField(max_length=254)),
                ('creado_el', models.DateTimeField(auto_now_add=True)),
                ('destinatario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensajes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
