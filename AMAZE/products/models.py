from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=200)
    main_category  = models.CharField(max_length=200)
    sub_category  = models.CharField(max_length=200)
    image  = models.CharField(max_length=200)
    link  = models.CharField(max_length=200)
    ratings = models.CharField(max_length=200,null=True,blank=True)
    no_of_ratings = models.CharField(max_length=200,null=True,blank=True)
    discount_price  = models.CharField(max_length=200,null=True,blank=True)
    actual_price  = models.CharField(max_length=200)

    def __str__(self):
        return self.name


