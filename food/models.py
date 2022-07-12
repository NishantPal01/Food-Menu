from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Items(models.Model):

    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default='https://images.unsplash.com/photo-1614332287897-cdc485fa562d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8Y29taW5nJTIwc29vbnxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60')

    def __str__(self):
        return self.item_name


    def get_absolute_url(self):
        return reverse("details", kwargs={"pk": self.pk})
