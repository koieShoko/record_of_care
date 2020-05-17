# Generated by Django 2.2.12 on 2020-05-05 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0004_auto_20200505_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='notice',
            field=models.CharField(blank=True, max_length=8000, null=True, verbose_name='特記事項'),
        ),
        migrations.AlterField(
            model_name='record',
            name='resident',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='record.Resident', verbose_name='利用者'),
        ),
        migrations.AlterField(
            model_name='record',
            name='staff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='職員'),
        ),
        migrations.AlterField(
            model_name='record',
            name='translated_notice',
            field=models.CharField(blank=True, max_length=8000, null=True, verbose_name='変換結果'),
        ),
    ]
