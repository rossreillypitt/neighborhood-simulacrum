# Generated by Django 3.2.5 on 2021-08-20 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indicators', '0033_alter_variable_aggregation_method'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='objectslayer',
            name='maplayer_ptr',
        ),
        migrations.RemoveField(
            model_name='parcelslayer',
            name='maplayer_ptr',
        ),
        migrations.AlterField(
            model_name='maplayer',
            name='visible',
            field=models.BooleanField(verbose_name='Visible by default'),
        ),
        migrations.DeleteModel(
            name='GeogChoroplethMapLayer',
        ),
        migrations.DeleteModel(
            name='ObjectsLayer',
        ),
        migrations.DeleteModel(
            name='ParcelsLayer',
        ),
    ]