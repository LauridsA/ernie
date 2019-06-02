# Generated by Django 2.2 on 2019-06-01 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0005_auto_20190601_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='state',
            field=models.CharField(choices=[('SUCCESS', 'SUCCESS'), ('FAILED', 'FAILED'), ('TIMEOUT', 'TIMEOUT'), ('IN_PROGRESS', 'IN_PROGRESS'), ('TO_DO', 'TO_DO')], default='TO_DO', max_length=200),
        ),
    ]