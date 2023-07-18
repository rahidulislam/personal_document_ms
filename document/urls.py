from django.urls import path
from document import views

app_name = 'document'

urlpatterns = [
    path('list-upload/', views.DocumentListCreateView.as_view(), name='list_create_doucment'),
]