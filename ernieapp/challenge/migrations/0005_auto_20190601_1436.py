# Generated by Django 2.2 on 2019-06-01 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0004_auto_20190601_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='ID',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]
