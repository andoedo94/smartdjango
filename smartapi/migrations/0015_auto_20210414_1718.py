# Generated by Django 3.1.6 on 2021-04-14 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartapi', '0014_auto_20210414_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='creation_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='creation_hour',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='lang',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
