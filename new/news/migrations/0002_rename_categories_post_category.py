# Generated by Django 5.0.7 on 2024-09-21 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='categories',
            new_name='category',
        ),
    ]