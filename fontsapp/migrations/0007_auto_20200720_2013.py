# Generated by Django 3.0.6 on 2020-07-20 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fontsapp', '0006_auto_20200720_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='font',
            name='output_photo1',
            field=models.ImageField(blank=True, null=True, upload_to='output/'),
        ),
    ]
