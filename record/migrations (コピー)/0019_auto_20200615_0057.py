# Generated by Django 2.2.12 on 2020-06-14 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0018_auto_20200615_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal_record',
            name='form2',
            field=models.IntegerField(choices=[(0, '0/10'), (1, '1/10'), (2, '2/10'), (3, '3/10'), (4, '4/10'), (5, '5/10'), (6, '6/10'), (7, '7/10'), (8, '8/10'), (9, '9/10'), (10, '10/10')], default=10, verbose_name='主食量'),
        ),
        migrations.AlterField(
            model_name='meal_record',
            name='form3',
            field=models.IntegerField(choices=[(0, '0/10'), (1, '1/10'), (2, '2/10'), (3, '3/10'), (4, '4/10'), (5, '5/10'), (6, '6/10'), (7, '7/10'), (8, '8/10'), (9, '9/10'), (10, '10/10')], default=10, verbose_name='副食量'),
        ),
    ]
