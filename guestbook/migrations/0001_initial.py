# Generated by Django 2.2.1 on 2019-05-27 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guestbook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=32)),
                ('message', models.CharField(max_length=2000)),
                ('regdate', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
