# Generated by Django 4.0.4 on 2022-05-31 00:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_articlemodel_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlemodel',
            name='author',
        ),
    ]
