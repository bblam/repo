# Generated by Django 2.0.4 on 2018-04-27 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_auto_20180427_0729'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='show',
            field=models.IntegerField(default=0),
        ),
    ]