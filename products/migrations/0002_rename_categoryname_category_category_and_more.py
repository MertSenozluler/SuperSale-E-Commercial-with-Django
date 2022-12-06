# Generated by Django 4.1.2 on 2022-11-10 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='categoryName',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='subcategory',
            old_name='subCategoryName',
            new_name='subCategory',
        ),
        migrations.AlterField(
            model_name='products',
            name='subCategory',
            field=models.ManyToManyField(to='products.subcategory'),
        ),
    ]
