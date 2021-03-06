# Generated by Django 4.0.5 on 2022-06-09 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('arrived_at', models.DateField()),
                ('price', models.IntegerField()),
                ('unit', models.CharField(max_length=32)),
                ('arrived_from', models.CharField(max_length=64)),
            ],
        ),
    ]
