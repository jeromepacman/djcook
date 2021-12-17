# Generated by Django 3.2.10 on 2021-12-16 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BotUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('chat_id', models.CharField(max_length=64)),
                ('username', models.CharField(blank=True, max_length=64, null=True)),
                ('first_name', models.CharField(blank=True, max_length=64, null=True)),
                ('last_name', models.CharField(blank=True, max_length=64, null=True)),
                ('language_code', models.CharField(blank=True, max_length=8, null=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_blocked_bot', models.BooleanField(default=False)),
                ('last_action_datetime', models.DateTimeField(blank=True, null=True)),
                ('language', models.CharField(blank=True, choices=[('FR', 'fr'), ('EN', 'en')], default=None, max_length=2, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
