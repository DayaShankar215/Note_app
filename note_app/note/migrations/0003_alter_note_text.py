# Generated by Django 5.2 on 2025-05-04 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0002_alter_note_is_completed_alter_note_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='text',
            field=models.CharField(max_length=200),
        ),
    ]
