from django.shortcuts import render
from django.views import generic

from django.contrib.auth.mixins import LoginRequiredMixin
#from .models import Producto

'''class CategoriaView(LoginRequiredMixin, generic.ListView):
    model = Producto
    template_name = "inv/categoria_list.html"
    context_object_name = "obj"
    Login_url = "bases:login"
'''