from django.db import models

# Create your models here.
class SpinningMills(models.Model):
    spinningmills_id = models.AutoField(primary_key=True)
    spinningmills_document = models.CharField('Nro. Documento', max_length=20)
    spinningmills_business_name = models.CharField('Razón Social', max_length=100)
    spinningmills_address = models.CharField('Dirección', max_length=200)
    spinningmills_name = models.CharField('Nombres', max_length=30)
    spinningmills_lastname = models.CharField('Apellidos', max_length=50)
    spinningmills_phone = models.CharField('Teléfono', max_length=13, null=True, blank=True)
    spinningmills_email = models.EmailField('Correo', max_length=254, null=True, blank=True)
    spinningmills_enabled = models.IntegerField('Habilitado', default=1)
    created_at = models.DateTimeField('Creado', auto_now_add=True)
    updated_at = models.DateTimeField('Actualizado', auto_now=True)

    def __str__(self):
        return '{0} - {1}'.format(self.spinningmills_id, self.spinningmills_business_name)
