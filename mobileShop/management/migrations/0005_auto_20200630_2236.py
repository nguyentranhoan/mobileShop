# Generated by Django 3.0.7 on 2020-06-30 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_auto_20200630_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobilephone',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
