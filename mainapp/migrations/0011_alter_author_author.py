# Generated by Django 4.2.7 on 2023-11-24 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_alter_quote_author_alter_quote_topics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='author',
            field=models.CharField(max_length=50, unique=True, verbose_name='Author'),
        ),
    ]
