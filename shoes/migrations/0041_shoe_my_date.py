# Generated by Django 5.0.4 on 2024-05-23 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0040_remove_boot_date_remove_catooni_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoe',
            name='my_date',
            field=models.DateField(null=True),
        ),
    ]
