# Generated by Django 3.0.8 on 2020-08-23 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule_builder', '0008_auto_20200823_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectedenrollment',
            name='graduation_plan',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='projected_enrollments', to='schedule_builder.GraduationPlan'),
        ),
        migrations.AlterField(
            model_name='projectedenrollment',
            name='subject',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='projected_enrollments', to='schedule_builder.Subject'),
        ),
    ]
