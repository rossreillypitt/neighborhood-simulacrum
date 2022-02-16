# Generated by Django 3.2.9 on 2021-12-21 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public_housing', '0008_alter_projectindex_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='HouseCatSubsidyListing',
            fields=[
                ('id', models.IntegerField(db_column='_id', primary_key=True, serialize=False)),
                ('property_id', models.TextField(blank=True, null=True)),
                ('subsidy_data_source', models.TextField(blank=True, null=True)),
                ('hud_property_name', models.TextField(blank=True, null=True)),
                ('subsidy_expiration_date', models.TextField()),
            ],
            options={
                'db_table': '6803b4c9-df5d-4ef0-8c33-43e9feaff0a2',
                'managed': False,
            },
        ),
    ]