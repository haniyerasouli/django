# Generated by Django 5.0.4 on 2024-05-22 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0036_boot_catooni'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='boot',
            options={'verbose_name': 'بوت', 'verbose_name_plural': 'بوت ها'},
        ),
        migrations.AlterModelOptions(
            name='catooni',
            options={'verbose_name': 'کتونی', 'verbose_name_plural': 'کتونی ها '},
        ),
    ]
