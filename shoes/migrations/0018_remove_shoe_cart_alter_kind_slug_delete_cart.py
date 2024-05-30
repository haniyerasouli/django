# Generated by Django 5.0.4 on 2024-05-17 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0017_cart_remove_shoe_production_date_shoe_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoe',
            name='cart',
        ),
        migrations.AlterField(
            model_name='kind',
            name='slug',
            field=models.CharField(db_index=True, default='', max_length=25, unique=True, verbose_name='اسلاگ در url'),
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]