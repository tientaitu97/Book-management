# Generated by Django 3.0.7 on 2020-06-26 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_management', '0005_auto_20200626_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publishingYear',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
