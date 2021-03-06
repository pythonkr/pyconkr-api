# Generated by Django 2.2 on 2019-04-25 13:34

from django.db import migrations, models


def init_ticket_setting(apps, schema_editor):
    ticket_setting = apps.get_model("api", "TicketSetting")
    ticket_setting.objects.create()

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0035_ticketsetting'),
    ]

    operations = [
        migrations.RunPython(init_ticket_setting),
    ]
