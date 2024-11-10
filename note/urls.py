from django.urls import reverse, path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('newnotes/', views.newnotes, name='newnotes'),
    path('notes/', views.notes, name='notes'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('updateNote', views.updateNote, name='updateNote'),
    # path('updateNote/<int:id>', views.updateNote, name='updateNote'),
]