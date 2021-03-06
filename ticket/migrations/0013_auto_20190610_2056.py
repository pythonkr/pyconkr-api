# Generated by Django 2.2 on 2019-06-10 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0012_auto_20190609_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='reason',
            field=models.CharField(blank=True, help_text='결재 실패 시 실패 사유를 저장합니다.', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('ready', 'ready'), ('paid', 'paid'), ('cancelled', 'cancelled'), ('error', 'error')], default='ready', max_length=10),
        ),
    ]
