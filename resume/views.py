from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Component
from .forms import PostForm
from django.urls import reverse_lazy
from django.contrib import messages

class Index(ListView):
    model = Component
    template_name = 'index.html'
    context_object_name = 'component_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['component_list'] = Component.objects.all()
        context['form'] = PostForm()
        return context

class AddComponent(CreateView):
    model = Component
    form_class = PostForm
    template_name = 'index.html'
    # login_url = reverse_lazy('login')
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        messages.success(self.request, 'Component added successfully!')
        return super().form_valid(form)