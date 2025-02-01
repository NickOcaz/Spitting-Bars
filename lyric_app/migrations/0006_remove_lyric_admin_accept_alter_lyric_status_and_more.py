# Generated by Django 4.2.18 on 2025-02-01 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lyric_app', '0005_lyric_admin_accept_alter_lyric_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lyric',
            name='admin_accept',
        ),
        migrations.AlterField(
            model_name='lyric',
            name='status',
            field=models.IntegerField(choices=[(0, 'Personal'), (1, 'Published')], default=0),
        ),
        migrations.AlterField(
            model_name='postapproval',
            name='status',
            field=models.IntegerField(choices=[(0, 'Personal'), (1, 'Published')], default=0),
        ),
    ]
