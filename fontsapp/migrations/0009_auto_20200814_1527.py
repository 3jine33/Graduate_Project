# Generated by Django 3.0.6 on 2020-08-14 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fontsapp', '0008_font_no_checkpoint'),
    ]

    operations = [
        migrations.AddField(
            model_name='font',
            name='input_photo3',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='font',
            name='input_photo4',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='font',
            name='input_photo5',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='font',
            name='input_photo6',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='font',
            name='input_photo7',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='font',
            name='input_photo8',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='font',
            name='input_photo9',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
