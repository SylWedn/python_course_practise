# Generated by Django 4.2.6 on 2023-10-31 18:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate_number', models.CharField(max_length=10, unique=True)),
                ('vin_code', models.CharField(max_length=100, unique=True)),
                ('client', models.CharField(max_length=100)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='pictures', verbose_name='Picture')),
                ('description', tinymce.models.HTMLField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=20, unique=True)),
                ('model', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('total_price', models.IntegerField()),
                ('date_due', models.DateField(null=True)),
                ('status', models.CharField(blank=True, choices=[('a', 'Confirmed'), ('b', 'In progress'), ('c', 'Completed'), ('d', 'Canceled')], default='a', help_text='Status', max_length=1)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='project_management.car')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='project_management.order')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='project_management.service')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='car_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='project_management.carmodel'),
        ),
    ]
