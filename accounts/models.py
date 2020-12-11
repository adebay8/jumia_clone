from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Detail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f"{self.user.username}'s Detail"

class Card(models.Model):
    card_number = models.CharField(max_length=16)
    expiry_date = models.DateField()

    def __str__(self):
        return '{}'.format(self.card_number)

class Order(models.Model):
    order_number = models.CharField(primary_key=True, max_length=20)
    shipped_date = models.DateField()
    estimated_delivery_date = models.DateField()

    def __str__(self):
        return '{}'.format(self.order_number)

class Profile(models.Model):
    card = models.OneToOneField(Card, on_delete=models.CASCADE)
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    detail = models.OneToOneField(Detail, on_delete=models.CASCADE)

    def __str__(self):
        return "{}'s Profile".format(self.detail.user.username)

    


