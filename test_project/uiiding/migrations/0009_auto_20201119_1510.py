# Generated by Django 3.1.3 on 2020-11-19 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uiiding', '0008_auto_20201119_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mother',
            name='number',
            field=models.CharField(blank=True, default='414F677983', max_length=255, primary_key=True, serialize=False, unique=True),
        ),
    ]
