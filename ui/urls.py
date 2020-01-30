from django.urls import path
from ui.views import index, uilogout, test

urlpatterns = [
    path('', index, name='index'),
    path('test',test,name = 'test'),
    path('logout', uilogout, name='logout')    
]
