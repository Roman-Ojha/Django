# Generated by Django 4.1.3 on 2022-12-13 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_examcenter_student2'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamCenter2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=70)),
                ('city', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='MyExampleCenter',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('school.examcenter2',),
        ),
    ]