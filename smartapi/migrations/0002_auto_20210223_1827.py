# Generated by Django 3.1.6 on 2021-02-23 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smartapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='citie',
            name='link',
        ),
        migrations.RemoveField(
            model_name='citie',
            name='url',
        ),
        migrations.AlterField(
            model_name='citie',
            name='down',
            field=models.DecimalField(decimal_places=999, max_digits=999),
        ),
        migrations.AlterField(
            model_name='citie',
            name='latitude',
            field=models.DecimalField(decimal_places=999, max_digits=999),
        ),
        migrations.AlterField(
            model_name='citie',
            name='left',
            field=models.DecimalField(decimal_places=999, max_digits=999),
        ),
        migrations.AlterField(
            model_name='citie',
            name='longitude',
            field=models.DecimalField(decimal_places=999, max_digits=999),
        ),
        migrations.AlterField(
            model_name='citie',
            name='right',
            field=models.DecimalField(decimal_places=999, max_digits=999),
        ),
        migrations.AlterField(
            model_name='citie',
            name='up',
            field=models.DecimalField(decimal_places=999, max_digits=999),
        ),
        migrations.CreateModel(
            name='LinkCity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.IntegerField(choices=[(1, 'Tripadvisor'), (2, 'Booking')])),
                ('value', models.CharField(max_length=150)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='smartapi.citie')),
            ],
        ),
    ]