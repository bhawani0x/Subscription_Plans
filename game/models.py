from django.db import models
from django.contrib.auth.models import User
from util.choices import PLAN_TYPE


# Create your models here.
class CommonModelFieldsBase(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    class Meta:
        abstract = True


# Create your models here.
class Customer(CommonModelFieldsBase):
    user = models.OneToOneField(User, on_delete=models.CASCADE, )
    choice = models.CharField(max_length=10, choices=PLAN_TYPE)

    def __str__(self):
        return str(self.user.first_name) + ' ' + str(self.user.last_name)
