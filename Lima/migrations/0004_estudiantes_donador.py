# Generated by Django 3.2.3 on 2021-06-04 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lima', '0003_auto_20210602_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiantes',
            name='donador',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
