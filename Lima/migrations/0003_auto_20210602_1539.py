# Generated by Django 3.2.3 on 2021-06-02 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lima', '0002_auto_20210531_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiantes',
            name='cuidad',
            field=models.CharField(default=True, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='estudiantes',
            name='apellidos',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='estudiantes',
            name='edad',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='estudiantes',
            name='nombres',
            field=models.CharField(max_length=100),
        ),
    ]
