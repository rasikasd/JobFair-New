# Generated by Django 2.2.4 on 2020-11-24 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='contact',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='jobs',
            name='email',
            field=models.EmailField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='jobdescription',
            field=models.TextField(max_length=100),
        ),
    ]
