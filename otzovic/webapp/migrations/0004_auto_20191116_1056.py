# Generated by Django 2.2.7 on 2019-11-16 10:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20191116_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='point',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Оценка'),
        ),
    ]
