# Generated by Django 5.0.2 on 2024-04-20 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fahrschulemanager_fullstack', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Forms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('vorname', models.CharField(max_length=255, null=True)),
                ('bezahlt', models.CharField(max_length=255, null=True)),
                ('datum', models.DateField()),
            ],
        ),
    ]
