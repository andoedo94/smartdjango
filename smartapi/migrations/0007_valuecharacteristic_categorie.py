# Generated by Django 3.1.6 on 2021-03-26 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smartapi', '0006_auto_20210326_0003'),
    ]

    operations = [
        migrations.AddField(
            model_name='valuecharacteristic',
            name='categorie',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='categorie', to='smartapi.categories'),
            preserve_default=False,
        ),
    ]
