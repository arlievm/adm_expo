# Generated by Django 3.2.9 on 2023-05-20 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page_en', '0002_placeofficeen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='placeen',
            name='city',
        ),
        migrations.AddField(
            model_name='placeen',
            name='address',
            field=models.CharField(default=1, max_length=255, verbose_name='Адрес'),
            preserve_default=False,
        ),
    ]
