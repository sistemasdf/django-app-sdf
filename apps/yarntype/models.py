from django.db import models
from apps.spinningmills.models import SpinningMills

# Create your models here.
class YarnType(models.Model):
    yarntype_id = models.AutoField(primary_key=True)
    spinningmills = models.ForeignKey(SpinningMills, on_delete=models.CASCADE)
    yarntype_name = models.CharField('Nombre de Producto', max_length=30)
    bag_volumen = models.IntegerField('Nro Bolsas', default=0)
    kg_volumen = models.FloatField('Kg', default=0.0)
    yarntype_enabled = models.IntegerField('Habilitado', default=1)
    created_at = models.DateTimeField('Creado', auto_now_add=True)
    updated_at = models.DateTimeField('Actualizado', auto_now=True)

    def __str__(self):
        return '{0} - {1} - {2}'.format(self.yarntype_id, self.spinningmills, self.yarntype_name)
