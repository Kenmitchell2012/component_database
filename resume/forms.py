from django import forms
from .models import Component

class PostForm(forms.ModelForm):
    class Meta:
        model = Component
        fields = ('name', 'lot_number', 'expiration_date', 'crt_part_number')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control bg-dark text-light'}),
            'lot_number': forms.TextInput(attrs={'class': 'form-control bg-dark text-light'}),
            'expiration_date': forms.DateInput(attrs={'class': 'form-control bg-dark text-light'}),
            'crt_part_number': forms.TextInput(attrs={'class': 'form-control bg-dark text-light'}),
        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        choices = Component.objects.all().values_list('name', 'name')
        choice_list = [(choice[0], choice[1]) for choice in choices]
        self.fields['name'].widget.choices = choice_list
