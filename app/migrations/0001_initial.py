# Generated by Django 2.2.6 on 2019-11-27 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=20)),
                ('subcategory', models.CharField(max_length=20)),
                ('brandname', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('image', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='tblregister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=2)),
                ('dob', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=100)),
                ('uname', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'tblregister',
            },
        ),
    ]
