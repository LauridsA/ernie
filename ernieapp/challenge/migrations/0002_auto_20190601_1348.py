# Generated by Django 2.2 on 2019-06-01 11:48

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
            field=models.CharField(choices=[(challenge.models.StatesClass('SUCCESS'), 'SUCCESS'), (challenge.models.StatesClass('FAILED'), 'FAILED'), (challenge.models.StatesClass('TIMEOUT'), 'TIMEOUT'), (challenge.models.StatesClass('IN_PROGRESS'), 'IN_PROGRESS'), (challenge.models.StatesClass('TO_DO'), 'TO_DO')], max_length=200),
        ),
    ]
