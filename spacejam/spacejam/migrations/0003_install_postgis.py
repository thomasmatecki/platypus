# Generated by Django 4.0.2 on 2022-02-13 20:45

from django.contrib.postgres.operations import CreateExtension
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("spacejam", "0002_space_image"),
    ]

    operations = [
        CreateExtension("postgis"),
    ]
