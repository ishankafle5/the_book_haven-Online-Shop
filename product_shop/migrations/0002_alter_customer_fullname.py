# Generated by Django 4.2.3 on 2023-07-16 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='fullname',
            field=models.CharField(blank=True, max_length=255, null=None),
        ),
    ]