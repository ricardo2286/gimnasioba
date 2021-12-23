from django.http.response import HttpResponse
from django.shortcuts import render
from AppGimnasio.models import musculacion, yoga, natacion

# Create your views here.
def inicio(request):
   return render(request,'AppGimnasio/inicio.html')

def musculacion(request):
    return render(request, 'AppGimnasio/musculacion.html')

def yoga(request):
    return render(request,'AppGimnasio/yoga.html')    

def natacion(request):
    return render(request,'AppGimnasio/natacion.html')    


def musculacionformulario(request):
    if request.method == "POST":
      musculacioninsta = musculacion(request.POST["nombre"], request.POST["apellido"])

      musculacioninsta.save()
        
      return render(request, 'AppGimnasio/inicio.html')
      
    return render(request, 'AppGimnasio/musculacionformulario.html')
    
    