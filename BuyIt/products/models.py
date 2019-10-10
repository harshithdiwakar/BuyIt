import random
import os
from django.db import models
from django.db.models.signals import pre_save
from .utils import unique_slug_generator

def get_file_ext(filepath):
    base_name = os.path.basename(filepath)
    name,ext = os.path.splitext(base_name)
    return name,ext

def upload_image_path(instance,filename):
    new_filename = random.randint(1,1000)
    name,ext = get_file_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename,ext=ext)
    return "products/product_images/{final_filename}".format(final_filename=final_filename)

class ProductQueryset(models.query.QuerySet):
    def featured(self):
        return self.filter(featured=True)

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQueryset(self.model, using=self._db)

    def featured(self):
        return self.get_queryset().filter(featured=True)


    def get_by_id(self,id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

class Product(models.Model):
    title       = models.CharField(max_length=50,null=True)
    slug        = models.SlugField(blank=True,unique=True,primary_key=True)
    description = models.TextField()
    price       = models.DecimalField(decimal_places=2,max_digits=30)
    image       = models.ImageField(upload_to=upload_image_path,null=True,blank=True)
    featured    = models.BooleanField(default=False)
    
    objects = ProductManager()

    def get_absolute_url(self):
        return "{slug}".format(slug=self.slug)

    def __str__(self):
        return self.title


def pre_save_create_slug(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_create_slug,sender=Product)

class Shop(models.Model):
    category = models.CharField(max_length=10)
    slug     = models.SlugField(blank=True,unique=True,primary_key=True)

    def __str__(self):
        return self.category

# class product_category(models.Model):
#     sub_category = models.CharField(max_length=20,null=True)
#     category     = models.ForeignKey(shop,on_delete=models.CASCADE)