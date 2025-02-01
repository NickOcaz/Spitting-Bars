from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('lyric_app', 'previous_migration_file'),  # Replace with the actual previous migration file
    ]

    operations = [
        migrations.AddField(
            model_name='lyric',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='lyric',
            name='is_protected',
            field=models.BooleanField(default=False),
        ),
    ]