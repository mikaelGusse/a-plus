# Generated by Django 4.2.13 on 2024-11-26 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0061_courseinstance_points_goal_enabled'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='studentmodulegoal',
            constraint=models.UniqueConstraint(fields=('student', 'module'), name='Unique student module goal'),
        ),
    ]
