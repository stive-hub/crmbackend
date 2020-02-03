from django.urls import path
from ui.views import index, uilogout

urlpatterns = [
    path('', index,name='index'),
    path('logout', uilogout, name='logout')    
]
