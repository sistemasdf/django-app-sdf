from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.weavers.models import Weavers

# Create your models here.
class User(AbstractUser):
    user_admin = models.IntegerField('Tipo de Usuario', default=0)
    weavers = models.ForeignKey(Weavers, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return '{0} {1}'.format(self.first_name,self.last_name)
