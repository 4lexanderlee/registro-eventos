from django.urls import path
from . import views

urlpatterns = [
    path('eventos/', views.EventoListCreateView.as_view(), name='evento-list-create'),
    path('eventos/<int:pk>/', views.EventoDetailView.as_view(), name='evento-detail'),
]