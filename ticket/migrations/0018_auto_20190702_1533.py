# Generated by Django 2.2 on 2019-07-02 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0017_auto_20190702_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketproduct',
            name='type',
            field=models.CharField(choices=[('C', '컨퍼런스'), ('G', '컨퍼런스 단체'), ('Y', '영코더'), ('B', '아이돌봄'), ('T', '튜토리얼'), ('S', '스프린트'), ('H', '체육시간')], default='C', max_length=1),
        ),
    ]
