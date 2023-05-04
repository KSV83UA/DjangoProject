# Generated by Django 4.2 on 2023-04-26 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0016_chief_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='galery',
            name='text',
            field=models.CharField(default=' ', max_length=255),
        ),
        migrations.AlterField(
            model_name='clients',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main_app.status'),
        ),
    ]
