# Generated by Django 3.0.7 on 2020-07-05 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='blog_description',
            field=models.CharField(default='', max_length=15000),
        ),
    ]
