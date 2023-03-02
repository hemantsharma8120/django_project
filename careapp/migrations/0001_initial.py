# Generated by Django 4.0.5 on 2022-07-25 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('discription', models.TextField()),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('discription', models.TextField()),
                ('image', models.ImageField(upload_to='images')),
                ('add_date', models.DateTimeField()),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='careapp.category')),
            ],
            options={
                'db_table': 'product',
            },
        ),
    ]