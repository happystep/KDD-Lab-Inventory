# Generated by Django 2.2 on 2019-11-07 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_category_location_stockcontrol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='cost_per_item',
            field=models.IntegerField(default=0),
        ),
    ]