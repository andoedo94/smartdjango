# Generated by Django 3.1.6 on 2021-04-14 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartapi', '0013_auto_20210414_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertweet',
            name='location',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='usertweet',
            name='time_zone',
            field=models.CharField(max_length=50, null=True),
        ),
    ]