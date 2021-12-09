# Generated by Django 4.0 on 2021-12-09 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='botuser',
            name='language_code',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='botuser',
            name='user_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='botuser',
            name='language',
            field=models.CharField(blank=True, choices=[('FR', 'fr'), ('EN', 'en')], default=None, max_length=2, null=True),
        ),
    ]