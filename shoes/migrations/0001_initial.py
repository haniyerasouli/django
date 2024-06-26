# Generated by Django 5.0.4 on 2024-04-20 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shoe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=30)),
                ('production_date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('photo', models.ImageField(upload_to='files/shoes')),
                ('brand', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=10)),
                ('slug', models.SlugField(default='')),
            ],
        ),
    ]
