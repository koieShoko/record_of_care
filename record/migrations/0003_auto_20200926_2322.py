# Generated by Django 3.0.7 on 2020-09-26 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0002_auto_20200926_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category_form1',
            name='label',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='項目名'),
        ),
    ]