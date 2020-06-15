# Generated by Django 2.2.12 on 2020-06-15 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0003_auto_20200615_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='time',
            field=models.TimeField(default='07:00', verbose_name='時刻'),
        ),
        migrations.AlterField(
            model_name='resident',
            name='unit',
            field=models.CharField(choices=[('東', '東'), ('西', '西')], default='東', max_length=1, verbose_name='ユニット'),
        ),
    ]
