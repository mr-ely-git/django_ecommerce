from django.db import models
from django.utils.text import slugify


class ProductCategory(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    slug = models.SlugField(max_length=100, unique=True, allow_unicode=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)


class ProductTag(models.Model):
    name: str = models.CharField(max_length=100, unique=True, db_index=True)
    slug = models.SlugField(max_length=100, unique=True, allow_unicode=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)


class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    short_description = models.CharField(max_length=400)
    description = models.TextField()
    slug = models.SlugField(max_length=100, unique=True, allow_unicode=True, db_index=True, blank=True)
    is_publish = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    category = models.ManyToManyField(ProductCategory, related_name='products')
    tag = models.ManyToManyField(ProductTag, related_name='products', blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)
