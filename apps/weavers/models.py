from django.db import models

# Create your models here.
class Weavers(models.Model):
    weavers_id = models.AutoField(primary_key=True)
    weavers_document = models.CharField('Nro. Documento', max_length=20)
    business_name = models.CharField('Razón Social', max_length=100)
    fiscal_address = models.CharField('Dirección Fiscal', max_length=200)
    delivery_address = models.CharField('Dirección de Entrega', max_length=200)
    weavers_name = models.CharField('Nombres', max_length=30)
    weavers_lastname = models.CharField('Apellidos', max_length=50)
    weavers_phone = models.CharField('Teléfono', max_length=13, null=True, blank=True)
    weavers_email = models.EmailField('Correo', max_length=254, null=True, blank=True)
    weavers_enabled = models.IntegerField('Habilitado', default=1)
    created_at = models.DateTimeField('Creado', auto_now_add=True)
    updated_at = models.DateTimeField('Actualizado', auto_now=True)

    def __str__(self):
        return '{0} - {1}'.format(self.weavers_id, self.business_name)
