# Generated by Django 4.2.7 on 2023-11-25 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_alter_author_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='SimpleContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Enter Email')),
                ('problem', models.CharField(choices=[('problem_in_website', 'Regarding Website'), ('problem_in_quote', 'Regarding Quote'), ('problem_in_author', 'Regarding Author'), ('problem_in_other', 'Anything Else')], max_length=50, verbose_name='What is the Problem here')),
            ],
            options={
                'verbose_name': 'SimpleContact',
                'verbose_name_plural': 'SimpleContacts',
            },
        ),
    ]
