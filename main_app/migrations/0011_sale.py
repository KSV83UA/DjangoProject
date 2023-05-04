# Generated by Django 4.2 on 2023-04-19 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_alter_dishes_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_stop', models.DateField(blank=True)),
            ],
            options={
                'verbose_name': ('Акції',),
                'verbose_name_plural': 'Акція',
                'ordering': (['date_start'],),
            },
        ),
    ]
