# Generated by Django 2.1.4 on 2020-07-20 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20200716_1722'),
    ]

    operations = [
        migrations.CreateModel(
            name='Myapp_person',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'myapp_person',
            },
        ),
    ]
