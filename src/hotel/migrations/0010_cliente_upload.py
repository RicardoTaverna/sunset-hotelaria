# Generated by Django 3.2.8 on 2021-11-13 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0009_auto_20211113_0115'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='upload',
            field=models.ImageField(null=True, upload_to='uploads/'),
        ),
    ]
