# Generated by Django 4.1.3 on 2022-11-26 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='comment',
            field=models.CharField(default='Not Available', max_length=100),
        ),
    ]
