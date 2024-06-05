from django.db import models


class UploadedImage(models.Model):
    image = models.ImageField(upload_to='images/')
    # Additional fields can be added if needed
