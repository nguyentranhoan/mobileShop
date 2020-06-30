# Generated by Django 3.0.7 on 2020-06-30 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='firm',
            name='description',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='firm',
            name='title',
            field=models.CharField(help_text='Enter a firm name (e.g. SAMSUNG, iPhone, Huawei, etsc.)', max_length=30, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='mobilephone',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='mobilephone',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='mobilephone',
            name='firm',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.Firm'),
        ),
        migrations.AddField(
            model_name='mobilephone',
            name='main_photo',
            field=models.ImageField(blank=True, null=True, upload_to='phones'),
        ),
        migrations.AddField(
            model_name='mobilephone',
            name='price',
            field=models.PositiveIntegerField(blank=True, help_text='Enter price of product, min=10000', null=True),
        ),
        migrations.AddField(
            model_name='mobilephone',
            name='title',
            field=models.CharField(default='Tên Thiết bị', help_text='Enter a name of Product', max_length=200, unique=True),
        ),
        migrations.AddField(
            model_name='mobilephone',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
    ]