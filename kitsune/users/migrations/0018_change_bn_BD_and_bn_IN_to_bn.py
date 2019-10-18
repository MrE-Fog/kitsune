# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-08-16 17:32
from __future__ import unicode_literals

from django.db import migrations


def change_locale_bn_bd_and_bn_in_to_bn_forwards(apps, schema_editor):
    Profile = apps.get_model('users', 'Profile')

    Profile.objects.all().filter(locale='bn-BD').update(locale='bn')
    # Change bn-IN profile to bn
    Profile.objects.all().filter(locale='bn-IN').update(locale='bn')


def change_locale_bn_to_bn_bd_backwards(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20190816_1732'),
    ]

    operations = [
        migrations.RunPython(change_locale_bn_bd_and_bn_in_to_bn_forwards,
                             change_locale_bn_to_bn_bd_backwards)
    ]