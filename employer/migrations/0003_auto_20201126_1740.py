# Generated by Django 2.2.4 on 2020-11-26 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0002_auto_20201124_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='jobdescription',
            field=models.TextField(max_length=400),
        ),
    ]
