# Generated by Django 3.2.9 on 2021-11-25 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_liked'),
    ]

    operations = [
        migrations.AddField(
            model_name='liked',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]