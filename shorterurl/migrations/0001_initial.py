# Generated by Django 3.1.3 on 2020-11-15 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True)),
                ('short_url', models.URLField(unique=True)),
                ('visits_count', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
    ]
