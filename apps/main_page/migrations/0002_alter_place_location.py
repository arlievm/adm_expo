# Generated by Django 3.2.9 on 2023-04-26 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='location',
            field=models.URLField(verbose_name='укажите ссылку координаты'),
        ),
    ]
