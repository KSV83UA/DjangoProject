# Generated by Django 4.2 on 2023-04-18 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_menu_descript'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='tab_target',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]