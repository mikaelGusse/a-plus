# Generated by Django 4.2.11 on 2024-08-13 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("exercise", "0050_submissiontagging"),
    ]

    operations = [
        migrations.AddField(
            model_name="revealrule",
            name="show_zero_points_immediately",
            field=models.BooleanField(
                default=False, verbose_name="LABEL_SHOW_ZERO_POINTS_IMMEDIATELY"
            ),
        ),
    ]
