# Generated by Django 2.1.7 on 2019-04-11 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='description',
            field=models.CharField(default='Przepis', max_length=5000),
        ),
    ]
