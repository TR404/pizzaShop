# Generated by Django 2.2.19 on 2021-03-30 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='pizzaShop/images')),
                ('small', models.CharField(max_length=10)),
                ('medium', models.CharField(max_length=10)),
                ('large', models.CharField(max_length=10)),
                ('description', models.TextField()),
            ],
        ),
    ]
