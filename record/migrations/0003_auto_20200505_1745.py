# Generated by Django 2.2.12 on 2020-05-05 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0002_auto_20200505_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='translated_notice',
            field=models.CharField(blank=True, max_length=8000, verbose_name='変換結果'),
        ),
    ]
