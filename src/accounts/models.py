from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

# Create your models here.
class CustomUser(AbstractUser):
  email = models.EmailField(_('email address'), unique=True)

  objects = CustomUserManager()

  def __str__(self):
    return self.email

class Membership(models.Model):
  name = models.CharField(max_length=100)
  priceId = models.CharField(max_length=255)

  def __str__(self):
    return f"{self.name} ({self.priceId})"

class StripeCustomer(models.Model):
  user = models.OneToOneField(to=CustomUser, on_delete=models.CASCADE)
  stripeCustomerId = models.CharField(max_length=255)
  stripeSubscriptionId = models.CharField(max_length=255)

  def __str__(self):
    return self.user.email