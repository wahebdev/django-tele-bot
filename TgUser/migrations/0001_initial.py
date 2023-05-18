# Generated by Django 4.2.1 on 2023-05-17 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TgUser',
            fields=[
                ('id', models.TextField(max_length=30, primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=30)),
                ('username', models.TextField(max_length=30)),
                ('phone', models.TextField(max_length=30)),
                ('long_lim', models.IntegerField()),
                ('size_lim', models.IntegerField()),
                ('message', models.TextField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='TgProcess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('process_id', models.TextField(max_length=30)),
                ('start_time', models.TextField(max_length=30)),
                ('messege_id', models.TextField(max_length=30)),
                ('end_time', models.TextField(max_length=30)),
                ('is_run', models.IntegerField()),
                ('process_user_constraint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TgUser.tguser')),
            ],
        ),
        migrations.CreateModel(
            name='TgMessageStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_text', models.TextField(max_length=30)),
                ('message_blob', models.BinaryField()),
                ('message_user_constraint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TgUser.tguser')),
            ],
        ),
    ]
