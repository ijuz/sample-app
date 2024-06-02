
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('create/',views.CreateContact,name='create'),
    path('profile/<pk>',views.Profile,name='profile'),
    path('edit/<pk>',views.EditContact,name='edit'),
    path('dlt/<pk>',views.DeleteContact,name='dlt')

]