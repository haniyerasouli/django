# Generated by Django 5.0.4 on 2024-05-21 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0027_remove_date_name_alter_date_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='date',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='قیمت'),
        ),
    ]
