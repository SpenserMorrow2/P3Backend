# Generated by Django 4.2.16 on 2024-10-28 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employeeid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, null=True)),
                ('type', models.TextField(blank=True, null=True)),
                ('employmentstatus', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]