from django.contrib import admin
from django.urls import path

from notes import views

urlpatterns = [
    path('',views.home,name='home'), 
    path('create/',views.create,name='create_note'),
    path('edit/<int:id>/',views.edit,name='edit_note'),
    path('view/<int:id>/',views.view_note,name='view_note'),
    path('delete/<int:id>/',views.delete_note,name='delete_note'),
]