# Generated by Django 4.2 on 2023-04-26 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0017_status_alter_galery_text_alter_clients_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='main_app.status'),
        ),
    ]
