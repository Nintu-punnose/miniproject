# Generated by Django 4.2.4 on 2023-08-17 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('useremail', models.EmailField(max_length=254)),
                ('usernumber', models.CharField(max_length=20)),
                ('userrole', models.CharField(max_length=20)),
                ('userpassword', models.CharField(max_length=100)),
            ],
        ),
    ]
