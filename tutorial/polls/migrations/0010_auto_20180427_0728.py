# Generated by Django 2.0.4 on 2018-04-27 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20180427_0709'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voted',
            name='question',
        ),
        migrations.AddField(
            model_name='question',
            name='voted',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='polls.Voted'),
            preserve_default=False,
        ),
    ]
