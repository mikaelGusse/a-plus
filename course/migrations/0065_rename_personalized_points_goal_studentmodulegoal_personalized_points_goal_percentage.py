# Generated by Django 4.2.11 on 2024-08-01 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0064_alter_studentmodulegoal_personalized_points_goal"),
    ]

    operations = [
        migrations.RenameField(
            model_name="studentmodulegoal",
            old_name="personalized_points_goal",
            new_name="personalized_points_goal_percentage",
        ),
    ]
