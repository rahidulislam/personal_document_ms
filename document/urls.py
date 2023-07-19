from django.urls import path
from document import views

app_name = 'document'

urlpatterns = [
    path('list-upload/', views.DocumentListCreateView.as_view(), name='list_create_doucment'),
    path('<int:pk>/',views.DocumentRetrieveUpdateDestroyView.as_view(), name='retrieve_update_delete'),
    path('<int:pk>/share/',views.DocumentShareView.as_view(), name='share_document'),
]