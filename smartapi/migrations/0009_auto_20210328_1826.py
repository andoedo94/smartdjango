# Generated by Django 3.1.6 on 2021-03-28 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartapi', '0008_node_relation_relationway_way_waynode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='id_node',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='relation',
            name='id_relation',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='way',
            name='id_way',
            field=models.BigIntegerField(),
        ),
    ]
