# Generated by Django 4.1.2 on 2022-11-10 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_categoryname_category_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='sellerOrBuyer',
        ),
        migrations.DeleteModel(
            name='SellerOrBuyer',
        ),
    ]