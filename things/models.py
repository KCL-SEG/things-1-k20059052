from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Thing(models.Model):
    name = models.CharField(max_length=30, unique = True, blank = False)

    description = models.CharField( unique = False, blank = True, max_length = 120)

    quantity = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(100)])
