from django.urls import path
from document import views

app_name = 'document'

urlpatterns = [
    path('list-upload/', views.DocumentListCreateView.as_view(), name='list_create_doucment'),
    path('<int:pk>/',views.DocumentRetrieveUpdateDestroyView.as_view(), name='retrieve_update_delete'),
    path('<int:pk>/share/',views.DocumentShareView.as_view(), name='share_document'),
    path('<int:pk>/share/user-list/', views.DocumentSharedWithUserView.as_view(), name='shared_user_list'),
    path('<int:pk>/download/',views.DocumentDownloadView.as_view(), name='download_document'),
]