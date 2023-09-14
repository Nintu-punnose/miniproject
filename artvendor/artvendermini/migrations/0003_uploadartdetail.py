# Generated by Django 4.2.4 on 2023-09-06 10:56

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('artvendermini', '0002_userdata_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadArtDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('art_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('art_type', models.CharField(max_length=255)),
                ('size', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('year', models.PositiveIntegerField()),
                ('image', models.ImageField(upload_to='art_images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png'])])),
                ('certificate', models.FileField(upload_to='art_certificates/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])])),
                ('description', models.TextField()),
            ],
        ),
    ]