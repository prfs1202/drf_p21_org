from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Model, CharField
from django.utils.text import slugify


class SlugBaseModel(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        abstract = True

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        while self.__class__.objects.filter(slug=self.slug).exists():
            self.slug += '1'
        super().save(force_insert, force_update, using, update_fields)


class Category(SlugBaseModel):
    pass


class User(AbstractUser):
    class Type(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        STAFF = 'staff', 'Staff'
        USER = 'user', 'User'

    type = models.CharField(max_length=10, choices=Type.choices, default=Type.USER)


class Product(SlugBaseModel):
    price = models.IntegerField()
    discount = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='products/', blank=True)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey('apps.Category', models.CASCADE)
    owner = models.ForeignKey('apps.User', models.SET_NULL, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)
# class ProductHistory(Model):
#     name = CharField(max_length=255)
#     action = CharField(max_length=255)
#     price = models.IntegerField()
#     deleted_at = models.DateTimeField(auto_now=True)
#