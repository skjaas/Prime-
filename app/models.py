from django.db import models
import datetime
# Create your models here.

class tblregister(models.Model):
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=2)
    dob = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    uname = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    class Meta:
        db_table = "tblregister"


class  product(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=20)
    subcategory = models.CharField(max_length=20)
    brandname = models.CharField(max_length=20)
    price = models.IntegerField()
    image = models.CharField(max_length=1000)
    class Meta:
        db_table = "product"

class laptop(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=20)
    subcategory = models.CharField(max_length=20)
    brandname = models.CharField(max_length=20)
    price = models.IntegerField()
    image = models.CharField(max_length=1000)
    class Meta:
        db_table = "laptop"

class powersupply(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=20)
    subcategory = models.CharField(max_length=20)
    brandname = models.CharField(max_length=20)
    price = models.IntegerField()
    image = models.CharField(max_length=1000)
    class Meta:
        db_table = "powersupply"

class headphone(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=20)
    subcategory = models.CharField(max_length=20)
    brandname = models.CharField(max_length=20)
    price = models.IntegerField()
    image = models.CharField(max_length=1000)
    class Meta:
        db_table = "headphone"


class motherboard(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=20)
    subcategory = models.CharField(max_length=20)
    brandname = models.CharField(max_length=20)
    price = models.IntegerField()
    image = models.CharField(max_length=1000)
    class Meta:
        db_table = "motherboard"

class memory(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=20)
    subcategory = models.CharField(max_length=20)
    brandname = models.CharField(max_length=20)
    price = models.IntegerField()
    image = models.CharField(max_length=1000)
    class Meta:
        db_table = "memory"

class storage(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=20)
    subcategory = models.CharField(max_length=20)
    brandname = models.CharField(max_length=20)
    price = models.IntegerField()
    image = models.CharField(max_length=1000)
    class Meta:
        db_table = "storage"

class coolingsystem(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=20)
    subcategory = models.CharField(max_length=20)
    brandname = models.CharField(max_length=20)
    price = models.IntegerField()
    image = models.CharField(max_length=1000)
    class Meta:
        db_table = "coolingsystem"


class graphicscard(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=20)
    subcategory = models.CharField(max_length=20)
    brandname = models.CharField(max_length=20)
    price = models.IntegerField()
    image = models.CharField(max_length=1000)
    class Meta:
        db_table = "graphicscard"

class monitor(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=20)
    subcategory = models.CharField(max_length=20)
    brandname = models.CharField(max_length=20)
    price = models.IntegerField()
    image = models.CharField(max_length=1000)
    class Meta:
        db_table = "monitor"

class cabinetcase(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=20)
    subcategory = models.CharField(max_length=20)
    brandname = models.CharField(max_length=20)
    price = models.IntegerField()
    image = models.CharField(max_length=1000)
    class Meta:
        db_table = "cabinetcase"


class processor(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=20)
    subcategory = models.CharField(max_length=20)
    brandname = models.CharField(max_length=20)
    price = models.IntegerField()
    image = models.CharField(max_length=1000)
    class Meta:
        db_table = "processor"