# Generated by Django 3.1.6 on 2021-04-14 14:49

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smartapi', '0010_tweet_usertweet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='geography',
            field=django.contrib.gis.db.models.fields.PointField(null=True, srid=4326),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='point',
            field=django.contrib.gis.db.models.fields.PointField(null=True, srid=4326),
        ),
    ]
