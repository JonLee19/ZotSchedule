# Generated by Django 3.0.8 on 2020-08-25 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule_builder', '0014_projectedenrollment_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='graduationplan',
            name='start_year',
            field=models.IntegerField(default=2019),
        ),
    ]
