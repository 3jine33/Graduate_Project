# Generated by Django 3.0.6 on 2020-08-31 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fontsapp', '0011_font_final_phrase'),
    ]

    operations = [
        migrations.AddField(
            model_name='font',
            name='create_later',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
