# Generated by Django 3.0.8 on 2020-08-25 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule_builder', '0012_auto_20200823_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectedenrollment',
            name='term',
            field=models.CharField(default='Fall', max_length=7),
        ),
    ]