# Generated by Django 5.0.4 on 2024-05-21 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0026_date_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='date',
            name='name',
        ),
        migrations.AlterField(
            model_name='date',
            name='created_at',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
