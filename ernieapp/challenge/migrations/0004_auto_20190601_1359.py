# Generated by Django 2.2 on 2019-06-01 11:59

import challenge.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0003_auto_20190601_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='state',
            field=models.CharField(choices=[(challenge.models.StatesClass('SUCCESS'), 'SUCCESS'), (challenge.models.StatesClass('FAILED'), 'FAILED'), (challenge.models.StatesClass('TIMEOUT'), 'TIMEOUT'), (challenge.models.StatesClass('IN_PROGRESS'), 'IN_PROGRESS'), (challenge.models.StatesClass('TO_DO'), 'TO_DO')], default='TO_DO', max_length=200),
        ),
    ]
