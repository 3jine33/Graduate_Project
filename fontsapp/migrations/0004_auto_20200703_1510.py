# Generated by Django 3.0.6 on 2020-07-03 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fontsapp', '0003_auto_20200525_2153'),
    ]

    operations = [
        migrations.RenameField(
            model_name='font',
            old_name='phrase',
            new_name='phrase1',
        ),
        migrations.AddField(
            model_name='font',
            name='input_photo2',
            field=models.ImageField(blank=True, null=True, upload_to='input/'),
        ),
        migrations.AddField(
            model_name='font',
            name='phrase2',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='font',
            name='template_img',
            field=models.ImageField(blank=True, null=True, upload_to='template_img/'),
        ),
    ]
