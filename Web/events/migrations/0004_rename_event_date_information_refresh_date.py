# Generated by Django 4.1.1 on 2022-09-19 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0003_information_interest"),
    ]

    operations = [
        migrations.RenameField(
            model_name="information", old_name="event_date", new_name="refresh_date",
        ),
    ]