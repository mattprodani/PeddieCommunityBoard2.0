# Generated by Django 3.1.7 on 2021-03-08 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peddieforum', '0007_auto_20210307_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click Read More to read post!', max_length=255),
        ),
    ]