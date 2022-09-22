from django.db import models

class Product(models.Model):
    flavor = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True)
    quantity = models.IntegerField()
    available = models.BooleanField()
    glueten_free = models.BooleanField()
    lactose_free = models.BooleanField()
    non_dairy = models.BooleanField()

class Guest(models.Model):
    guest_id = models.IntegerField(primary_key=True)
    address = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    zip_code = models.IntegerField()
    phone_number = models.IntegerField()
    product = models.ManyToManyField(Product, through='Order')

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    order_date = models.DateField(auto_now_add=True)
    quantity = models.IntegerField()
