from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Proveedor
from provider.forms import ProveedorForm

class ProveedorView(LoginRequiredMixin, generic.ListView):
    model = Proveedor
    template_name = 'provider/proveedor_list.html'
    context_object_name = "obj"
    login_url = "bases:login"

class ProveedorNew(LoginRequiredMixin, generic.ListView):
    model = Proveedor
    template_name = 'provider/proveedor_list.html'
    context_object_name = "obj"
    form_class = ProveedorForm
    success_url = reverse_lazy('provider:proveedor_list')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.User
        print(self.request.user.id)
        return super().form_valid(form)
class ProveedorEdit(LoginRequiredMixin, generic.ListView):
    model = Proveedor
    template_name = 'provider/proveedor_form.html'
    context_object_name = "obj"
    form_class = ProveedorForm
    success_url = reverse_lazy('provider:proveedor_list')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.User
        print(self.request.user.id)
        return super().form_valid(form)

    

