from .views import Homview , Formsview  ,DDetailview ,UUpdateView
from django.urls import path,include 


# app_name = 'main'
urlpatterns = [
    
    path('',Homview.as_view(),name='home'),
    path('forms',Formsview.as_view(),name='forms'),
    path('detail/<int:pk>' , DDetailview.as_view() ,name = 'maqola'),
    path('edit/<int:pk>' , UUpdateView.as_view() ,name = 'edit'),
    
]