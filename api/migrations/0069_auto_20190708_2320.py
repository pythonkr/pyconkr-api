# Generated by Django 2.2 on 2019-07-08 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0068_remove_sprint_num_of_participants'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_organizer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_volunteer',
            field=models.BooleanField(default=False),
        ),
    ]
