# Generated by Django 3.2.9 on 2021-12-21 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0011_rename_common_geoid_adminregion_global_geoid'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminregion',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True),
        ),
    ]