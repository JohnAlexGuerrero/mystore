# Generated by Django 2.2.4 on 2020-10-08 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(verbose_name='date created')),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
            ],
        ),
    ]
