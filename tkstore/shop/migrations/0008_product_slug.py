# Generated by Django 3.2.5 on 2021-07-13 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_alter_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=True, max_length=100),
        ),
    ]
