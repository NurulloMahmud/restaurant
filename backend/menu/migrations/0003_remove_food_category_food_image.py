# Generated by Django 4.2.7 on 2024-01-11 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_alter_food_available_qty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='category',
        ),
        migrations.AddField(
            model_name='food',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
