from django import forms
from business.models import Business, BusinessEntry

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full py-4 px-6 rounded-xl border'}),
        }

class BusinessEntryForm(forms.ModelForm):
    class Meta:
        model = BusinessEntry
        fields = ['business', 'entry_type', 'description', 'amount', 'date']
        widgets = {
            'business': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl border'}),
            'entry_type': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl border'}),
            'description': forms.Textarea(attrs={'class': 'w-full py-4 px-6 rounded-xl border'}),
            'amount': forms.NumberInput(attrs={'class': 'w-full py-4 px-6 rounded-xl border'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'w-full py-4 px-6 rounded-xl border'}),
        }

