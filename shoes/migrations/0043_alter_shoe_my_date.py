# Generated by Django 5.0.4 on 2024-05-23 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0042_alter_shoe_my_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoe',
            name='my_date',
            field=models.DateField(null=True),
        ),
    ]
