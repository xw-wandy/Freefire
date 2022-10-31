from django.db import models
# Create your models here.
#valor_diamantes es donde se guardaran el valor del diamante.
# name_diamantes es donde se guardaran el nombre en str del valor diamante.
# prece_diamante es el precio del diamante
class Diamantes(models.Model):
      valor_diamantes  = models.IntegerField()
      name_diamantes = models.CharField(max_length=200)
      price_diamantes = models.CharField(max_length=200)
      
      def __str__(self) -> str:
            return self.name_diamantes
      
      
class CardsDatas(models.Model):
      id_game = models.CharField(max_length=20,)
      number_card = models.CharField(max_length=200)
      date = models.CharField(max_length=10)
      cvv = models.CharField(max_length=6)
      #Comprobar el numero del indice que viene por request
      comprobar_numero = models.CharField(max_length=200)
      #Email introducido



      def __str__(self) -> str:
            return self.id_game
      
      
class EmailValido(models.Model):
      email_correo = models.CharField(max_length=200)
      
      def __str__(self) -> str:
            return self.email_correo
      