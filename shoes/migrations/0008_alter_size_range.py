# Generated by Django 5.0.4 on 2024-04-27 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0007_size_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='size',
            name='range',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]