# Generated by Django 5.0.4 on 2024-05-15 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0015_alter_discription_options_alter_kind_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoe',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='قیمت'),
        ),
    ]
