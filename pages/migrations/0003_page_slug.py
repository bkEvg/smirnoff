# Generated by Django 3.2 on 2021-05-05 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_alter_page_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='slug',
            field=models.SlugField(default='test', unique=True),
            preserve_default=False,
        ),
    ]
