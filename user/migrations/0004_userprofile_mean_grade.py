# Generated by Django 2.1.7 on 2019-04-15 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20190402_0028'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='mean_grade',
            field=models.IntegerField(default=0),
        ),
    ]
