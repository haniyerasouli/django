# Generated by Django 5.0.4 on 2024-04-27 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0008_alter_size_range'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='size',
            name='slug',
        ),
    ]
