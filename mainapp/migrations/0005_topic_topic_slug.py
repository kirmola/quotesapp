# Generated by Django 4.2.7 on 2023-11-22 14:49

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_alter_quote_quote_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='topic_slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, populate_from='topic'),
        ),
    ]
