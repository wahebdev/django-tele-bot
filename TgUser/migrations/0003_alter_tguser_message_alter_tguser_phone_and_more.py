# Generated by Django 4.2.1 on 2023-05-17 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TgUser', '0002_tguser_admin_tguser_block_tguser_spf_msg_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tguser',
            name='message',
            field=models.TextField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='tguser',
            name='phone',
            field=models.TextField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='tguser',
            name='username',
            field=models.TextField(blank=True, max_length=30),
        ),
    ]
