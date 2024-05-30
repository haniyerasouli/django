# Generated by Django 5.0.4 on 2024-05-22 12:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0030_alter_date_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoe',
            name='date',
        ),
        migrations.AddField(
            model_name='shoe',
            name='created_at',
            field=models.DateTimeField(default='2/3/2022', null=True, verbose_name='تاریخ تولید'),
        ),
        migrations.CreateModel(
            name='Pashneboland',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=30, verbose_name='برند')),
                ('property', models.CharField(max_length=30, verbose_name='ویژگی')),
                ('color', models.CharField(max_length=30, verbose_name='رنگ')),
                ('created_at', models.DateTimeField(default='2/3/2022', null=True, verbose_name='تاریخ تولید')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='قیمت')),
                ('photo', models.ImageField(upload_to='files/shoes', verbose_name='عکس')),
                ('gender', models.CharField(max_length=10, verbose_name='جنسیت')),
                ('slug', models.CharField(db_index=True, default='', max_length=50, verbose_name='اسلاگ در url')),
                ('discription', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shoes.discription', verbose_name='توضیح')),
                ('kind', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shoes.kind', verbose_name='جنس رویه')),
                ('size', models.ManyToManyField(to='shoes.size', verbose_name='اندازه')),
            ],
            options={
                'verbose_name': 'پاشنه بلند',
                'verbose_name_plural': 'پاشنه بلندها',
            },
        ),
        migrations.DeleteModel(
            name='Date',
        ),
    ]