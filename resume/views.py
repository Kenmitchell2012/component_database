from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Component
from .forms import PostForm, EditForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils import timezone
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Component
from django.db.models import Q
from datetime import datetime

# def ajax_search(request):
#     query = request.GET.get('q', '').strip()
#     if query:
#         components = Component.objects.filter(
#             Q(name__icontains=query) |
#             Q(lot_number__icontains=query) |
#             Q(crt_part_number__icontains=query)
#         )
#     else:
#         components = Component.objects.all()   
#     html = render_to_string('components_table.html', {'component_list': components})
#     return JsonResponse({'html': html})



def ajax_search(request):
    query = request.GET.get('q', '').strip()
    if query:
        components = Component.objects.filter(
            Q(name__icontains=query) |
            Q(lot_number__icontains=query) |
            Q(crt_part_number__icontains=query)
        )
    else:
        components = Component.objects.all()
    
    # Prepare the context with the necessary data
    current_date = datetime.now().strftime('%Y-%m-%d')
    context = {
        'component_list': components,
        'current_date': current_date,
        'user': request.user
    }
    
    html = render_to_string('components_table.html', context)
    return JsonResponse({'html': html})



class Index(ListView):
    model = Component
    template_name = 'index.html'
    context_object_name = 'component_list'

    def get_queryset(self):
        return Component.objects.all().order_by('-date_added')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['component_list'] = Component.objects.all()
        context['form'] = PostForm()
        context['current_date'] = timezone.now().strftime('%m/%d/%Y')
        context['component_count'] = Component.objects.count()
        return context

class AddComponent(CreateView):
    model = Component
    form_class = PostForm
    template_name = 'index.html'
    # login_url = reverse_lazy('login')
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        response = super().form_valid(form)
        component_name = form.instance.name
        messages.success(self.request, f'Component "{component_name}" added successfully!')
        return response
    
class UpdateComponent(UpdateView):
    model = Component
    form_class = EditForm
    template_name = 'edit_component.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        response = super().form_valid(form)
        component_name = form.instance.name
        messages.success(self.request, f'Component "{component_name}" updated successfully!')
        return response

class DeleteComponent(DeleteView):
    model = Component
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, *args, **kwargs):
        context = super(DeleteComponent, self).get_context_data(*args, **kwargs)
        return context

class ComponentDetail(CreateView):
    pass