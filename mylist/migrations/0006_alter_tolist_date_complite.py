# Generated by Django 4.1.4 on 2023-01-27 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mylist", "0005_alter_tolist_date_complite"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tolist",
            name="date_complite",
            field=models.DateTimeField(default="", null=True),
        ),
    ]
