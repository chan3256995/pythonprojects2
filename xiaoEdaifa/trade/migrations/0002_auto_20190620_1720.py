# Generated by Django 2.2.1 on 2019-06-20 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refundapply',
            name='add_time',
            field=models.BigIntegerField(default=1561022416.3236341),
        ),
    ]
