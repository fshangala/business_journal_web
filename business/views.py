from django.views.generic import TemplateView, FormView, ListView
from business.forms import BusinessEntryForm, BusinessForm
from business.models import BusinessEntry

class HomeView(ListView):
    template_name='business/home.html'
    model=BusinessEntry
    context_object_name='entries'
    ordering=['-date']
    
class AddBusinessView(FormView):
    template_name='business/add_business.html'
    form_class=BusinessForm
    success_url='/'
    
    def form_valid(self,form):
        form.save()
        return super().form_valid(form)

class AddBusinessEntryView(FormView):
    template_name='business/add_business_entry.html'
    form_class=BusinessEntryForm
    success_url='/'
    
    def form_valid(self,form):
        form.save()
        return super().form_valid(form)
    