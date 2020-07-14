# Generated by Django 3.0.8 on 2020-07-13 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('department', models.CharField(max_length=8)),
                ('number', models.CharField(max_length=10)),
                ('code', models.IntegerField(default=0, verbose_name='Course Code')),
                ('type', models.CharField(max_length=10, verbose_name='Lecture, Discussion, Lab, or other')),
                ('section', models.CharField(max_length=2)),
                ('units', models.IntegerField(default=0)),
                ('instructor', models.CharField(max_length=30)),
                ('time', models.CharField(max_length=20)),
                ('place', models.CharField(max_length=15)),
                ('finals', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='CoursePlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
