# Generated by Django 4.0 on 2021-12-30 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('slug', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('slug', models.SlugField(unique=True)),
                ('model', models.CharField(max_length=30)),
                ('make', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='car_rentals.manufacturer')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
