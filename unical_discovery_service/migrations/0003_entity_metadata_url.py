# Generated by Django 2.2.3 on 2019-08-09 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unical_discovery_service', '0002_auto_20190711_0015'),
    ]

    operations = [
        migrations.AddField(
            model_name='entity',
            name='metadata_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
