from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.template import loader
from inicio.models import Zapatilla
from inicio.forms import CrearZapatillaFormulario

def inicio(request):
    
    #v2
    # template = loader.get_template('inicio.html')
    # template_renderizado = template.render({})
    
    # return HttpResponse(template_renderizado)

    #v3
    return render(request,  'inicio/inicio.html', {})

def zapatillas(request):
    
    marca_a_buscar = request.GET.get('marca')
    
    if marca_a_buscar:
        listado_de_zapatillas = Zapatilla.objects.filter(marca__icontains=marca_a_buscar)
    else:
        listado_de_zapatillas = Zapatilla.objects.all()
    
    
    return render(request, 'inicio/zapatillas.html', {'listado_de_zapatillas': listado_de_zapatillas})

def crear_zapatilla(request):
    
    # v1(HTML)
    # print('============')
    # print('GET')
    # print(request.GET)
    # print('============')
    # print('POST')
    # print(request.POST)
    
    # if request.method == 'POST':
    #     marca= request.POST.get('marca')
    #     descripcion= request.POST.get('descripcion')
    #     anio= request.POST.get('anio')

    #     zapatilla = Zapatilla(marca=marca, descripcion=descripcion, anio=anio)
    #     zapatilla.save()
    
    # v2 (Django forms)
    if request.method == 'POST':
        formulario = CrearZapatillaFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            marca= info_limpia.get('marca')
            descripcion= info_limpia.get('descripcion')
            anio= info_limpia.get('anio')
            
            zapatilla = Zapatilla(marca=marca, descripcion=descripcion, anio=anio)
            zapatilla.save()
            
            return redirect('zapatillas')
        else:
            return render(request, 'inicio/crear_zapatilla.html', {'formulario': formulario})
        
    formulario = CrearZapatillaFormulario()
    return render(request, 'inicio/crear_zapatilla.html', {'formulario': formulario})
    