# Generated by Django 4.1.7 on 2023-04-04 21:46

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
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pelicula', models.CharField(max_length=40)),
                ('titulo', models.CharField(max_length=80)),
                ('texto', models.TextField()),
                ('fecha', models.DateField()),
                ('poster', models.ImageField(upload_to='')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
