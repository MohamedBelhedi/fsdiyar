# Generated by Django 5.0.6 on 2024-05-09 09:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fahrschulemanager_fullstack', '0010_alter_prüflinge_prüfungsdatum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prüflinge',
            name='prüfungsdatum',
            field=models.DateField(default=datetime.datetime(2024, 5, 9, 11, 39, 59, 710692)),
        ),
    ]
