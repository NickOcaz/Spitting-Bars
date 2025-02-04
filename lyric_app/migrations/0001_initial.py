# Generated by Django 4.2.18 on 2025-02-01 21:12
# Generated by Django 4.2.18 on 2025-02-02 11:32


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
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Rap', 'Rap'), ('Song', 'Song'), ('Poem', 'Poem'), ('Other', 'Other')], default='Rap', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Lyric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('lyric', models.TextField()),
                ('status', models.IntegerField(choices=[(0, 'Personal'), (1, 'Publish Me (needs admin approval)')], default=0)),
                ('is_protected', models.BooleanField(default=False)),
                ('is_approved', models.BooleanField(default=False)),
                ('admin_accept', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('artist', models.ForeignKey(on_delete=models.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('genre', models.ForeignKey(on_delete=models.CASCADE, to='lyric_app.Genre')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='PostApproval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Personal'), (1, 'Publish Me (needs admin approval)')], default=0)),
                ('approved_by', models.ForeignKey(on_delete=models.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('lyric', models.OneToOneField(on_delete=models.CASCADE, to='lyric_app.Lyric')),
            ],
        ),
    ]
