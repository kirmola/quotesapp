# Generated by Django 4.2.7 on 2023-11-22 07:01

from django.db import migrations
import shortuuid.django_fields


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_alter_quote_quote_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='quote_id',
            field=shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvwxyz123456790', editable=False, length=6, max_length=45, prefix='', primary_key=True, serialize=False),
        ),
    ]
