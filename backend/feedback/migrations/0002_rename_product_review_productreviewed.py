# Generated by Django 4.0.4 on 2022-08-18 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='product',
            new_name='productReviewed',
        ),
    ]