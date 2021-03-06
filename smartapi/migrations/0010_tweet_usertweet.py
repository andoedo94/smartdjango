# Generated by Django 3.1.6 on 2021-04-14 12:54

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smartapi', '0009_auto_20210328_1826'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(max_length=10, null=True)),
                ('time_zone', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('duration', models.IntegerField(null=True)),
                ('is_bot', models.BooleanField(null=True)),
                ('estancia', models.IntegerField(null=True)),
                ('is_tourist', models.BooleanField(null=True)),
                ('usuarios_id', models.BigIntegerField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usercity', to='smartapi.city')),
            ],
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('creation_date', models.DateField()),
                ('creation_hour', models.TimeField()),
                ('lang', models.CharField(max_length=10)),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('geography', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='twcity', to='smartapi.city')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usertweet', to='smartapi.usertweet')),
            ],
        ),
    ]
