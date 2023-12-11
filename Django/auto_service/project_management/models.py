from django.db import models
from django.contrib.auth.models import User
from datetime import date
from tinymce.models import HTMLField


class CarModel(models.Model):
    make = models.CharField(max_length=20, unique=True, null=False)
    model = models.CharField(max_length=50, unique=True, null=False)

    def __str__(self):
        return f"{self.make} {self.model}"


class Car(models.Model):
    plate_number = models.CharField(max_length=10, unique=True, null=False)
    car_model = models.ForeignKey(CarModel, null=False, on_delete=models.PROTECT)
    vin_code = models.CharField(max_length=100, unique=True, null=False)
    client = models.CharField(max_length=100, null=False)
    picture = models.ImageField('Picture', upload_to='pictures', null=True, blank=True)
    description = HTMLField(default='')

    def __str__(self):
        return f"{self.plate_number}"


class Service(models.Model):
    name = models.CharField(max_length=30, null=False)
    price = models.IntegerField(null=False)

    def __str__(self):
        return f"{self.name}"


class Order(models.Model):
    date = models.DateField(null=False)
    car = models.ForeignKey(Car, null=False, on_delete=models.PROTECT)
    total_price = models.IntegerField(null=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_due = models.DateField(null=True)

    STATUS = (
        ('a', 'Confirmed'),
        ('b', 'In progress'),
        ('c', 'Completed'),
        ('d', 'Canceled'),
    )

    status = models.CharField(
        max_length=1,
        choices=STATUS,
        blank=True,
        default='a',
        help_text='Status',
    )

    @property
    def is_overdue(self):
        if self.date_due and date.today() > self.date_due:
            return True
        return False

    def __str__(self):
        return f"{self.date}"


class OrderLine(models.Model):
    service = models.ForeignKey(Service, on_delete=models.PROTECT)
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    quantity = models.IntegerField(null=False)
    price = models.IntegerField(null=False)

    def __str__(self):
        return f"{self.quantity}"
