# Generated by Django 2.0.4 on 2018-04-27 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_question_show'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='votes',
            field=models.IntegerField(default=1),
        ),
    ]
