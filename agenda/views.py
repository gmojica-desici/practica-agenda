#from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse


def inicio(request):
    template = get_template("base.html")

    context = {
        "titulo": "Inicio"
    }

    return HttpResponse(template.render(context), request)
