# Generated by Django 4.1.4 on 2023-01-28 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mylist", "0007_alter_tolist_date_complite"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tolist",
            name="date_complite",
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
