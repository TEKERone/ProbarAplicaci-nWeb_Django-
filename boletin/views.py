from django.shortcuts import render
from .forms import ContactForm, RegModelForm
from .models import Registrado
from .forms import ContactForm

def inicio(request):
    titulo = "HOLA"
    if request.user.is_authenticated:
        titulo = "Bienvenido %s" %(request.user)
    form = RegModelForm(request.POST or None)
    
    context ={
        "titulo" : titulo,
        "el_form":form,
    }

    if form.is_valid():
        instance = form.save(commit=False)
        nombre = form.cleaned_data.get("nombre")
        email = form.cleaned_data.get("email")
        if not instance.nombre:
            instance.nombre = "PERSONA"
        instance.save()
        
        context={
            "titulo": "Gracias %s!" %(nombre)
        }
        if not nombre:
            context = {
                "titulo": "Gracias %s!" %(email)
            }

        print(instance)
        print(instance.timestamp)
        # form_data=form.cleaned_data
        # abc = form_data.get("email")
        # abc2= form_data.get("nombre")
        # obj = Registrado.objects.create(email=abc, nombre=abc2)
        
    
    return render(request, "inicio.html", context)


def constact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        for key, value in form.cleaned_data.items():
            print(key, value)
        # for key in form.cleaned_data:
        #     print(key)
        #     print(form.cleaned_data.get(key))
        # email = form.cleaned_data.get("email")
        # mensaje =form.cleaned_data.get("mensaje")
        # nombre =form.cleaned_data.get("nombre")
        # print(email,mensaje,nombre)
    context = {
        "form":form, 
    }
    return render(request, "forms.html", context)
