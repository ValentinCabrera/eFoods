# Generated by Django 4.2.7 on 2023-11-29 03:41

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0004_alter_orderdiscount_unique_together"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="orderdiscount",
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name="orderdiscount",
            name="discount",
        ),
        migrations.RemoveField(
            model_name="orderdiscount",
            name="order",
        ),
        migrations.DeleteModel(
            name="Discount",
        ),
        migrations.DeleteModel(
            name="OrderDiscount",
        ),
    ]
