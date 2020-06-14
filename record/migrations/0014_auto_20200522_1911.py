# Generated by Django 2.2.12 on 2020-05-22 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0013_auto_20200521_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal_record',
            name='form2',
            field=models.IntegerField(choices=[(0, '0分目'), (1, '1分目'), (2, '2分目'), (3, '3分目'), (4, '4分目'), (5, '5分目'), (6, '6分目'), (7, '7分目'), (8, '8分目'), (9, '9分目'), (10, '10分目')], default=10, verbose_name='主食摂取量'),
        ),
        migrations.AlterField(
            model_name='meal_record',
            name='form3',
            field=models.IntegerField(choices=[(0, '0分目'), (1, '1分目'), (2, '2分目'), (3, '3分目'), (4, '4分目'), (5, '5分目'), (6, '6分目'), (7, '7分目'), (8, '8分目'), (9, '9分目'), (10, '10分目')], default=10, verbose_name='副食摂取量'),
        ),
    ]
