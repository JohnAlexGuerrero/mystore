from django.db import models
#from ckeditor.fields import RichTextField


class Empresa(models.Model):
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField('date created')
    status = models.BooleanField('Status',default=True)
    def __str__(self):
        return self.name


'''class Factura(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
     = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)'''
# Create your models here.
