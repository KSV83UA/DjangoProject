# Generated by Django 4.2 on 2023-04-19 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_sale'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sale',
            options={'ordering': (['date_start', 'title'],), 'verbose_name': ('Акції',), 'verbose_name_plural': 'Акція'},
        ),
    ]
