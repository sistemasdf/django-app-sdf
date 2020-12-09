from django.db import models
from apps.orders.models import Order
from apps.yarntype.models import YarnType

# Create your models here.
class OrderDetail(models.Model):
    orderdetail_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    yarntype = models.ForeignKey(YarnType, on_delete=models.CASCADE)
    product_code = models.CharField('Código de Producto', max_length=20, null=True, blank=True)
    number_bag = models.IntegerField('Nro Bolsas', default=0)
    amount_kg = models.IntegerField('Cantidad Kg', default=0)
    orderdetail_enabled = models.IntegerField('Activo', default=1)
    created_at = models.DateTimeField('Creado', auto_now_add=True)
    updated_at = models.DateTimeField('Actualizado', auto_now=True)

    def __str__(self):
        return '{0} - {1} - {2}'.format(self.orderdetail_id, self.order, self.yarntype)
