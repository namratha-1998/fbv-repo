# Generated by Django 2.2 on 2020-12-08 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eno', models.IntegerField()),
                ('ename', models.CharField(max_length=40)),
                ('esal', models.IntegerField()),
                ('eaddr', models.CharField(max_length=100)),
            ],
        ),
    ]
