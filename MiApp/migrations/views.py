
from django.shortcuts import render
from .forms import Clase1Form

def clase1_view(request):
    form = Clase1Form()
    if request.method == 'POST':
        form = Clase1Form(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'clase1_templates.html', {'form': form})

from django.shortcuts import render
from .forms import Clase2Form

def clase2_form_view(request):
    form = Clase2Form()
    if request.method == 'POST':
        form = Clase2Form(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'clase2_form.html', {'form': form})

from django.shortcuts import render
from .forms import Clase3Form


def clase3_form_view(request):
    form = Clase3Form()
    if request.method == 'POST':
        form = Clase3Form(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'clase3_form.html', {'form': form})


from django.shortcuts import render
from .models import Clase1, Clase2, Clase3

def search_view(request):
    if request.method == 'GET':
        query = request.GET.get('query')  # Obtener el valor de búsqueda del formulario
        if query:
            # Realizar el filtrado en la base de datos usando Q objects
            results = clase1.objects.filter(campo1__icontains=query) | \
                      clase2.objects.filter(campo2__icontains=query) | \
                      clase3.objects.filter(campo3__icontains=query)
        else:
            results = []
    return render(request, 'search.html', {'results': results, 'query': query})