# Generated by Django 3.1.3 on 2020-11-19 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uiiding', '0011_auto_20201119_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mother',
            name='number',
            field=models.CharField(blank=True, default='FAA02FBD27', max_length=255, primary_key=True, serialize=False, unique=True),
        ),
    ]
