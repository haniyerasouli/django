# Generated by Django 5.0.4 on 2024-05-01 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0014_alter_discription_name_alter_kind_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='discription',
            options={'verbose_name': 'توضیح', 'verbose_name_plural': 'توضیحات'},
        ),
        migrations.AlterModelOptions(
            name='kind',
            options={'verbose_name': 'جنس رویه', 'verbose_name_plural': 'جنس های رویه'},
        ),
        migrations.AlterModelOptions(
            name='shoe',
            options={'verbose_name': 'کفش', 'verbose_name_plural': 'کفش ها'},
        ),
        migrations.AlterModelOptions(
            name='size',
            options={'verbose_name': 'اندازه', 'verbose_name_plural': 'اندازه ها'},
        ),
    ]
