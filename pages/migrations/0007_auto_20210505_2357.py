# Generated by Django 3.2 on 2021-05-05 16:57

from django.db import migrations, models
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_alter_page_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='description_de',
            field=models.CharField(max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='description_ru',
            field=models.CharField(max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='text_de',
            field=django_quill.fields.QuillField(null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='text_ru',
            field=django_quill.fields.QuillField(null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='title_de',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='title_ru',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
