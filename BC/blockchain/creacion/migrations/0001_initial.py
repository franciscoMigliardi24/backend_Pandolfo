# Generated by Django 3.0.3 on 2020-02-08 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bloque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.CharField(max_length=100)),
                ('archivo', models.CharField(max_length=100)),
                ('hashActual', models.CharField(max_length=100)),
                ('hashAnterior', models.CharField(max_length=100)),
            ],
        ),
    ]
