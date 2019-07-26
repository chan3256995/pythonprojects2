# Generated by Django 2.2.1 on 2019-06-20 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30, unique=True)),
                ('qq', models.BigIntegerField(null=True, unique=True)),
                ('email', models.CharField(max_length=30, null=True, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('type', models.SmallIntegerField(choices=[(1, '客户'), (2, '拿货人')], default=1)),
                ('phone', models.BigIntegerField(null=True, unique=True)),
                ('add_time', models.BigIntegerField(null=True)),
                ('balance', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=128)),
                ('add_time', models.BigIntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
        ),
    ]
