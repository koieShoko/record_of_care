# Generated by Django 3.0.7 on 2020-08-20 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0003_auto_20200722_2224'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='ruby_translated_notice',
            field=models.CharField(blank=True, default='', max_length=8000, verbose_name='変換結果'),
        ),
    ]
