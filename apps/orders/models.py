from django.db import models
from apps.spinningmills.models import SpinningMills
from apps.weavers.models import Weavers

SHIPPING_SCHEDULE_CHOICES = [
    (1, 'AM'),
    (2, 'PM'),
]

ORDER_STATUS_CHOICES = [
    (1, 'Recibido'),
    (2, 'Unidad Asignada'),
    (3, 'Recojo Exitoso'),
    (4, 'Entrega Exitosa'),
]

# Create your models here.
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    weavers = models.ForeignKey(Weavers, on_delete=models.CASCADE)
    spinningmills = models.ForeignKey(SpinningMills, on_delete=models.CASCADE)
    invoice = models.FileField(blank=False, null=False)
    invoice_name = models.CharField('Nombre de Factura', max_length=20)
    shipping_date = models.DateTimeField('Fecha de envío', null=True, blank=True)
    shipping_schedule = models.IntegerField('Horario de envío', choices=SHIPPING_SCHEDULE_CHOICES, default=1)
    order_date = models.DateTimeField('Fecha de Pedido', null=True, blank=True)
    order_status = models.IntegerField('Estado del Pedido', choices=ORDER_STATUS_CHOICES, default=1)
    order_enabled = models.IntegerField('Activo', default=1)
    created_at = models.DateTimeField('Creado', auto_now_add=True)
    updated_at = models.DateTimeField('Actualizado', auto_now=True)

    def __str__(self):
        return '{0} - {1}'.format(self.order_id, self.spinningmills)
