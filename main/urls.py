from .views import Homview , Formsview  ,DDetailview
from django.urls import path,include 


# app_name = 'main'
urlpatterns = [
    
    path('',Homview.as_view(),name='home'),
    path('forms',Formsview.as_view(),name='forms'),
    # path('delit/<int:id>/', DDeleteView.as_view(),name='delit')
    path('detail/<int:pk>' , DDetailview.as_view() ,name = 'maqola '),

    
]