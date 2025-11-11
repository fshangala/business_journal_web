from django.urls import path
from business.views import AddBusinessEntryView, AddBusinessView, HomeView

app_name="business"
urlpatterns=[
    path('',HomeView.as_view(),name='home'),
    path('add_business/',AddBusinessView.as_view(),name='add_business'),
    path('add_business_entry/',AddBusinessEntryView.as_view(),name='add_business_entry'),
    
]