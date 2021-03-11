# Generated by Django 3.1.5 on 2021-02-05 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indicators', '0006_auto_20210205_1734'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ckanvariable',
            name='field_in_carto',
        ),
        migrations.RemoveField(
            model_name='ckanvariable',
            name='sql_filter_for_carto',
        ),
        migrations.AddField(
            model_name='variable',
            name='field_in_carto',
            field=models.CharField(blank=True, help_text='If left blank, the value for "field" will be used.', max_length=60, null=True, verbose_name='Carto field'),
        ),
        migrations.AddField(
            model_name='variable',
            name='sql_filter_for_carto',
            field=models.TextField(blank=True, help_text='If left blank, the value for "sql filter" will be used.', null=True, verbose_name='Carto SQL Filter'),
        ),
    ]