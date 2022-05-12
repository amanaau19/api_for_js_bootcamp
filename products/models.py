from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Name')
    description = models.CharField(max_length=255, verbose_name='Description', null=True, blank=True)
    price = models.PositiveIntegerField(verbose_name='Price', blank=True, null=True)
    image = models.ImageField(upload_to='product-images/', blank=True, null=True, verbose_name='Photo')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f"{self.name}"
