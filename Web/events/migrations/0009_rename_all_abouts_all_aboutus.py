# Generated by Django 4.1.1 on 2022-09-25 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0008_all_abouts_alter_paper_papername"),
    ]

    operations = [
        migrations.RenameModel(old_name="all_abouts", new_name="all_aboutus",),
    ]