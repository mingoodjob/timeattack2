# Generated by Django 4.0.4 on 2022-05-31 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlemodel',
            name='category',
            field=models.CharField(max_length=256),
        ),
    ]
