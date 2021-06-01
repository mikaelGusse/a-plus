# Generated by Django 3.2.4 on 2021-07-01 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diploma', '0002_coursediplomadesign_availability'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursediplomadesign',
            name='availability',
            field=models.IntegerField(choices=[(1, 'INTERNAL_USERS'), (2, 'EXTERNAL_USERS'), (3, 'ALL_USERS')], default=2),
        ),
    ]
