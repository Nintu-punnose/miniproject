# Generated by Django 4.2.4 on 2023-09-11 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artvendermini', '0011_uploadartdetail_approval_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadartdetail',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
