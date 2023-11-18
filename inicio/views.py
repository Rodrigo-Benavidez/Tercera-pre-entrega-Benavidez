from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.template import loader
from inicio.models import Zapatilla
from inicio.forms import CrearZapatillaFormulario, BusquedaZapatillaFormulario, ActualizarZapatillaFormulario
from django.contrib.auth.decorators import login_required

def inicio(request):
    
    #v2
    # template = loader.get_template('inicio.html')
    # template_renderizado = template.render({})
    
    # return HttpResponse(template_renderizado)

    #v3
    return render(request, 'inicio/inicio.html', {})

def zapatillas(request):
    
    # v1
    # marca_a_buscar = request.GET.get('marca')
    
    # if marca_a_buscar:
    #     listado_de_zapatillas = Zapatilla.objects.filter(marca__icontains=marca_a_buscar)
    # else:
    #     listado_de_zapatillas = Zapatilla.objects.all()
    
    # v2
    formulario = BusquedaZapatillaFormulario(request.GET)
    if formulario.is_valid():
        marca_a_buscar = formulario.cleaned_data.get('marca')
        listado_de_zapatillas = Zapatilla.objects.filter(marca__icontains=marca_a_buscar)
    
    formulario = BusquedaZapatillaFormulario()
    return render(request, 'inicio/zapatillas.html', {'formulario': formulario, 'listado_de_zapatillas': listado_de_zapatillas})

@login_required
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

@login_required
def eliminar_zapatilla(request, zapatilla_id):
    zapatilla_a_eliminar = Zapatilla.objects.get(id=zapatilla_id)
    zapatilla_a_eliminar.delete()
    return redirect("zapatillas")

@login_required
def actualizar_zapatilla(request, zapatilla_id):
    zapatilla_a_actualizar = Zapatilla.objects.get(id=zapatilla_id)
    
    if request.method == "POST":
        formulario = ActualizarZapatillaFormulario(request.POST)
        if formulario.is_valid():
            info_nueva = formulario.cleaned_data
            
            zapatilla_a_actualizar.marca = info_nueva.get('marca')
            zapatilla_a_actualizar.descripcion = info_nueva.get('descripcion')
            zapatilla_a_actualizar.anio = info_nueva.get('anio')
            
            zapatilla_a_actualizar.save()
            return redirect('zapatillas')
        else:
            return render(request, 'inicio/actualizar_zapatilla.html', {'formulario': formulario})
            
     
    formulario = ActualizarZapatillaFormulario(initial={'marca': zapatilla_a_actualizar.marca, 'descripcion': zapatilla_a_actualizar.descripcion, 'anio': zapatilla_a_actualizar.anio})
    return render(request, 'inicio/actualizar_zapatilla.html', {'formulario': formulario})

def detalle_zapatilla(request, zapatilla_id):
    zapatilla = Zapatilla.objects.get(id=zapatilla_id)
    
    return render(request, 'inicio/detalle_zapatilla.html', {'zapatilla': zapatilla})

def about_me(request):
    return render(request, 'inicio/about_me.html', {})