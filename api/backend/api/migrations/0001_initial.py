# Generated by Django 3.0.3 on 2023-06-14 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=100)),
                ('Apellido', models.CharField(max_length=100)),
                ('Edad', models.PositiveIntegerField()),
                ('Ramo', models.CharField(max_length=100)),
                ('Profesor', models.CharField(max_length=100)),
            ],
        ),
    ]
