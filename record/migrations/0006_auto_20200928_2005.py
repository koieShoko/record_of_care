# Generated by Django 3.0.7 on 2020-09-28 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0005_auto_20200928_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='technical_noun',
            name='after',
            field=models.CharField(default='', max_length=1000, verbose_name='変換後（名詞）'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='technical_noun',
            name='before',
            field=models.CharField(max_length=1000, verbose_name='専門用語（名詞）'),
        ),
    ]
