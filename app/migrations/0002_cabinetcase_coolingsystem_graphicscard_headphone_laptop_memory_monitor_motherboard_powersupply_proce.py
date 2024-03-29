# Generated by Django 2.2.6 on 2019-11-27 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cabinetcase',
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
                'db_table': 'cabinnetcase',
            },
        ),
        migrations.CreateModel(
            name='coolingsystem',
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
                'db_table': 'coolingsystem',
            },
        ),
        migrations.CreateModel(
            name='graphicscard',
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
                'db_table': 'graphicscard',
            },
        ),
        migrations.CreateModel(
            name='headphone',
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
                'db_table': 'headphone',
            },
        ),
        migrations.CreateModel(
            name='laptop',
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
                'db_table': 'laptop',
            },
        ),
        migrations.CreateModel(
            name='memory',
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
                'db_table': 'memory',
            },
        ),
        migrations.CreateModel(
            name='monitor',
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
                'db_table': 'monitor',
            },
        ),
        migrations.CreateModel(
            name='motherboard',
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
                'db_table': 'motherboard',
            },
        ),
        migrations.CreateModel(
            name='powersupply',
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
                'db_table': 'powersupply',
            },
        ),
        migrations.CreateModel(
            name='processor',
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
                'db_table': 'processor',
            },
        ),
        migrations.CreateModel(
            name='storage',
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
                'db_table': 'storage',
            },
        ),
    ]
