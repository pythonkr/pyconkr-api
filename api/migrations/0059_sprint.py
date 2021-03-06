# Generated by Django 2.2 on 2019-06-24 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0058_presentation_secondary_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('program_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.Program')),
                ('opensource_desc', models.TextField(blank=True, default='')),
                ('opensource_url', models.CharField(blank=True, default='', max_length=255)),
                ('started_at', models.DateTimeField(blank=True, null=True)),
                ('finished_at', models.DateTimeField(blank=True, null=True)),
                ('submitted', models.BooleanField(default=False)),
                ('accepted', models.BooleanField(default=False)),
                ('place', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Place')),
            ],
            bases=('api.program',),
        ),
    ]
