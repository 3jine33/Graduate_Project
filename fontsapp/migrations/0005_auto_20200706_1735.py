# Generated by Django 3.0.6 on 2020-07-06 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fontsapp', '0004_auto_20200703_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='font',
            name='input_photo1',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='font',
            name='input_photo2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
