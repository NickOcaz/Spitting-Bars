# Generated by Django 4.2.18 on 2025-02-06 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lyric_app', '0004_lyric_admin_accept'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lyric',
            name='admin_accept',
            field=models.IntegerField(default=0),
        ),
    ]
