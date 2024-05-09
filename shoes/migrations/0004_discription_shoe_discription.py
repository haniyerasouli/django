# Generated by Django 5.0.4 on 2024-04-27 12:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0003_alter_shoe_production_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='shoe',
            name='discription',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shoes.discription'),
        ),
    ]