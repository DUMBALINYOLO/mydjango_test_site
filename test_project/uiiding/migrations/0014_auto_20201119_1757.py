# Generated by Django 3.1.3 on 2020-11-19 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uiiding', '0013_auto_20201119_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mother',
            name='number',
            field=models.CharField(blank=True, default='D6AC61A8B7', max_length=255, primary_key=True, serialize=False, unique=True),
        ),
    ]
