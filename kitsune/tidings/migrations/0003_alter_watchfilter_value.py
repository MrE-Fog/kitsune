# Generated by Django 4.1.9 on 2023-07-20 11:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tidings", "0001_squashed_0002_update_email_size"),
    ]

    operations = [
        migrations.AlterField(
            model_name="watchfilter",
            name="value",
            field=models.PositiveBigIntegerField(),
        ),
    ]
