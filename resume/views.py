from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Component
from .forms import PostForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils import timezone
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Component
from django.db.models import Q

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
    html = render_to_string('components_table.html', {'component_list': components})
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
        context['current_date'] = timezone.now().date()
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