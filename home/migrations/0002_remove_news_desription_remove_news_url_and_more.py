# Generated by Django 4.0.3 on 2022-03-20 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='desription',
        ),
        migrations.RemoveField(
            model_name='news',
            name='url',
        ),
        migrations.AddField(
            model_name='news',
            name='description',
            field=models.TextField(default='20.03.2022'),
            preserve_default=False,
        ),
    ]
