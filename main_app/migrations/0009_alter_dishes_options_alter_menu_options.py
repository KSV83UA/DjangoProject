# Generated by Django 4.2 on 2023-04-19 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_rename_descript_menu_content'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dishes',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='menu',
            options={'ordering': ['positions', 'title', 'time_created']},
        ),
    ]
