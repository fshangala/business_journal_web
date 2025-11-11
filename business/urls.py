from django.urls import path
from business.views import HomeView

app_name="business"
urlpatterns=[
    path('',HomeView.as_view(),name='home'),
]