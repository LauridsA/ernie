# Generated by Django 2.2 on 2019-06-01 10:20

import challenge.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='state',
            field=models.IntegerField(choices=[(challenge.models.States(1), 1), (challenge.models.States(2), 2), (challenge.models.States(3), 3), (challenge.models.States(4), 4), (challenge.models.States(5), 5)], default=challenge.models.States(5), max_length=6),
        ),
    ]