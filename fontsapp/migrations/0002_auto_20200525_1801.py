# Generated by Django 3.0.6 on 2020-05-25 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fontsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='font',
            name='phrase',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
