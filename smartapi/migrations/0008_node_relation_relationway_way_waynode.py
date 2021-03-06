# Generated by Django 3.1.6 on 2021-03-28 18:21

import django.contrib.postgres.fields.hstore
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smartapi', '0007_valuecharacteristic_categorie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=20, max_digits=30)),
                ('longitude', models.DecimalField(decimal_places=20, max_digits=30)),
                ('id_node', models.IntegerField()),
                ('tags', django.contrib.postgres.fields.hstore.HStoreField(null=True)),
                ('figure_points', models.CharField(max_length=1000, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categorynode', to='smartapi.categories')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='citiesnode', to='smartapi.city')),
            ],
        ),
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_relation', models.IntegerField()),
                ('tags', django.contrib.postgres.fields.hstore.HStoreField(null=True)),
                ('figure_points', models.CharField(max_length=1000, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoryrelation', to='smartapi.categories')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='citiesrelation', to='smartapi.city')),
            ],
        ),
        migrations.CreateModel(
            name='Way',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_way', models.IntegerField()),
                ('tags', django.contrib.postgres.fields.hstore.HStoreField(null=True)),
                ('is_end', models.BooleanField()),
                ('figure_points', models.CharField(max_length=1000, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoryway', to='smartapi.categories')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='citiesway', to='smartapi.city')),
            ],
        ),
        migrations.CreateModel(
            name='WayNode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smartapi.node')),
                ('way', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='waynode', to='smartapi.way')),
            ],
        ),
        migrations.CreateModel(
            name='RelationWay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relation_way', to='smartapi.relation')),
                ('way', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smartapi.way')),
            ],
        ),
    ]
