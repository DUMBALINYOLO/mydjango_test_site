# Generated by Django 3.1.3 on 2020-11-18 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uiiding', '0003_auto_20201118_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mother',
            name='number',
            field=models.UUIDField(default=122222, editable=False, primary_key=True, serialize=False, verbose_name='EBADE34E607F44E5B013'),
        ),
    ]
