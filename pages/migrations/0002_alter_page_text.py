# Generated by Django 3.2 on 2021-05-05 15:43

from django.db import migrations
import django_editorjs.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='text',
            field=django_editorjs.fields.EditorJsField(),
        ),
    ]
