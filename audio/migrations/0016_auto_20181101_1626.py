# Generated by Django 2.1 on 2018-11-01 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0015_remove_audio_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='title_author',
            field=models.CharField(max_length=5, null=True),
        ),
    ]