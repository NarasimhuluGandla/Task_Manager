# Generated by Django 5.1.3 on 2024-12-17 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_taskrestore'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact', models.IntegerField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('suggestions', models.TextField()),
            ],
        ),
    ]
