# Generated by Django 3.2.9 on 2023-04-26 12:03

from django.db import migrations
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0002_alter_place_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='location',
            field=location_field.models.plain.PlainLocationField(max_length=63),
        ),
    ]
