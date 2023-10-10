# Generated by Django 4.2.5 on 2023-09-28 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_categorymodel_alter_productmodel_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='category',
        ),
        migrations.AddField(
            model_name='productmodel',
            name='category',
            field=models.ManyToManyField(blank=True, null=True, to='products.categorymodel'),
        ),
    ]
