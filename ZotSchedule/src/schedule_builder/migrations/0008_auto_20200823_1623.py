# Generated by Django 3.0.8 on 2020-08-23 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule_builder', '0007_auto_20200722_0050'),
    ]

    operations = [
        migrations.CreateModel(
            name='GraduationPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Default Name', max_length=25)),
            ],
        ),
        migrations.DeleteModel(
            name='ClassSchedule',
        ),
        migrations.RemoveField(
            model_name='enrollment',
            name='course',
        ),
        migrations.RemoveField(
            model_name='enrollment',
            name='student',
        ),
        migrations.RemoveField(
            model_name='projectedenrollment',
            name='course_plan',
        ),
        migrations.RemoveField(
            model_name='student',
            name='courses',
        ),
        migrations.DeleteModel(
            name='CoursePlan',
        ),
        migrations.DeleteModel(
            name='Enrollment',
        ),
        migrations.AddField(
            model_name='graduationplan',
            name='subjects',
            field=models.ManyToManyField(related_name='graduation_plans', through='schedule_builder.ProjectedEnrollment', to='schedule_builder.Subject'),
        ),
        migrations.AddField(
            model_name='projectedenrollment',
            name='graduation_plan',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projected_enrollments', to='schedule_builder.GraduationPlan'),
        ),
    ]