# Generated by Django 5.1.4 on 2025-02-07 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestblood',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
