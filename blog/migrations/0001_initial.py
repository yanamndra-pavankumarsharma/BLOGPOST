# Generated by Django 5.1 on 2024-09-19 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=50)),
                ('slug', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]
