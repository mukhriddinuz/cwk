# Generated by Django 4.2.7 on 2024-10-30 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_aboutowner_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='courselevel',
            name='image',
            field=models.ImageField(default=0, upload_to='level_images/'),
            preserve_default=False,
        ),
    ]
