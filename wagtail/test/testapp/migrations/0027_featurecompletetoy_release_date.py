# Generated by Django 4.2.4 on 2023-08-21 10:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tests", "0026_featurecompletetoy"),
    ]

    operations = [
        migrations.AddField(
            model_name="featurecompletetoy",
            name="release_date",
            field=models.DateField(default=datetime.date.today),
        ),
    ]
