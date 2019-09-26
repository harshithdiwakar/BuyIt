import random
import os
from django.db import models
# from django.db.models.signals import pre_save
# from .utils import unique_pk_generator

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
    slug        = models.SlugField(blank=True)
    description = models.TextField()
    price       = models.DecimalField(decimal_places=2,max_digits=30)
    image       = models.ImageField(upload_to=upload_image_path,null=True,blank=True)
    featured    = models.BooleanField(default=False)
    
    objects = ProductManager()

    # def get_absolute_url(pk):
    #      return "products/{pk}/".format(pk=pk)
    #     return "products/{pk}/".format(pk=pk)

    def __str__(self):
        return self.title


# def pre_save_create_pk(sender,instance,*args,**kwargs):
#     if not instance.product_id:
#         instance.product_id = unique_pk_generator(instance)

# pre_save.connect(pre_save_create_pk,sender=Product)