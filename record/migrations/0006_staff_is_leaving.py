# Generated by Django 2.2.12 on 2020-06-15 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0005_record_is_leaving'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='is_leaving',
            field=models.BooleanField(default=False, verbose_name='退所済かどうか'),
        ),
    ]
