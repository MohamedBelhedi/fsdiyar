# Generated by Django 5.0.2 on 2024-04-20 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fahrschulemanager_fullstack', '0004_rename_forms_prüflinge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prüflinge',
            name='vorname',
        ),
    ]
