# Generated by Django 2.2 on 2019-07-21 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0071_auto_20190721_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='youngcoder',
            name='schedule_desc',
            field=models.CharField(blank=True, default='', help_text='일정을 설명하기 위한 필드입니다. e.g, 토요일 10시, 13시', max_length=255),
        ),
    ]
