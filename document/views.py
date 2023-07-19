from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Document
from .serializers import DocumentSerializer,DocumentShareSerializer
from personal_document_ms.permissions import IsOwner, IsOwnerOrAdminOnly

class DocumentListCreateView(generics.ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        if self.request.user.role == 1:
            return super().get_queryset()
        return super().get_queryset().filter(owner=self.request.user)
    
class DocumentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrAdminOnly)

class DocumentShareView(generics.UpdateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentShareSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    http_method_names = ('patch',)