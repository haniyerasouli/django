# Generated by Django 5.0.4 on 2024-05-22 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0037_alter_boot_options_alter_catooni_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='boot',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='catooni',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='pashneboland',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='shoe',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
