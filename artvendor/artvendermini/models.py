from django.db import models
from django.contrib.auth.models import User

class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userdata')
    role = models.CharField(max_length=20)
    number = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username

# class ArtPiece(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     art_name = models.CharField(max_length=100)
#     art_type = models.CharField(max_length=50)
#     art_size = models.CharField(max_length=20)
#     art_price = models.DecimalField(max_digits=10, decimal_places=2)
#     year = models.PositiveIntegerField()
#     art_image = models.ImageField(upload_to='art_images/')
#     art_certificate = models.FileField(upload_to='art_certificates/')
#     description = models.TextField()

#     def __str__(self):
#         return self.art_name