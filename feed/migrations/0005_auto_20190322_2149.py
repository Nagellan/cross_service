# Generated by Django 2.1.7 on 2019-03-22 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0004_auto_20190322_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='deadline',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='request',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]
