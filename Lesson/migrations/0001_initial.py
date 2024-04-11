# Generated by Django 5.0.4 on 2024-04-11 09:32

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Titre du cours', max_length=100)),
                ('description', models.CharField(default='Description du cours', max_length=300)),
                ('author', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Chapiter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Titre du chapitre', max_length=100)),
                ('content', models.CharField(default='Contenue du chapitre', max_length=300)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lesson.lesson')),
            ],
        ),
    ]