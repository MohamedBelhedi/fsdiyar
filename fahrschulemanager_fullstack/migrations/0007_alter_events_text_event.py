# Generated by Django 5.0.2 on 2024-04-21 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fahrschulemanager_fullstack', '0006_rename_prüfungsdatum_prüflinge_prüfungsdatum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='text_event',
            field=models.BigIntegerField(),
        ),
    ]
