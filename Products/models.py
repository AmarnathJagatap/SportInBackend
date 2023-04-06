from django.db import models


CATEGORY_CHOICES = (
    ('Leisure','Leisure'),
    ('Sports', 'Sports'),
)

class Products(models.Model):
    def nameFile(instance,filename):
        return '/'.join(['images', str(instance.category), filename])
    title = models.CharField(max_length=255,unique=True)
    discription = models.TextField()
    rate = models.IntegerField()
    category =  models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='Leisure')
    dimension = models.CharField(max_length=20)
    image = models.ImageField(upload_to=nameFile, blank=True, null=True)

    def __str__(self):
        return self.title
    