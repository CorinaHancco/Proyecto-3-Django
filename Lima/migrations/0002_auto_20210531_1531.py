# Generated by Django 3.2.3 on 2021-05-31 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lima', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiantes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.TextField()),
                ('apellidos', models.TextField()),
                ('edad', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Estudinates',
        ),
    ]
