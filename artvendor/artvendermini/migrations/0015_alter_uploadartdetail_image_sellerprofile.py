# Generated by Django 4.2.4 on 2023-09-16 09:04

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('artvendermini', '0014_remove_uploadartdetail_is_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadartdetail',
            name='image',
            field=models.ImageField(blank=True, upload_to='art_images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg', 'gif', 'bmp'])]),
        ),
        migrations.CreateModel(
            name='SellerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('pincode', models.CharField(max_length=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='seller_profile_images/')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('userdata', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='artvendermini.userdata')),
            ],
        ),
    ]