# Generated by Django 4.2.1 on 2023-05-17 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TgUser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tguser',
            name='admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tguser',
            name='block',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tguser',
            name='spf_msg',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='tgprocess',
            name='is_run',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='tguser',
            name='long_lim',
            field=models.IntegerField(default=7200),
        ),
        migrations.AlterField(
            model_name='tguser',
            name='size_lim',
            field=models.IntegerField(default=512),
        ),
    ]