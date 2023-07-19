from django.http import FileResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics, status, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from account.models import User
from .models import Document
from .serializers import DocumentSerializer, DocumentShareSerializer, DocumentShareUserSerializer
from personal_document_ms.permissions import IsOwner, IsOwnerOrAdminOnly


class DocumentListCreateView(generics.ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ['title', 'description', 'file_format', 'created_at']

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

    def update(self, request, *args, **kwargs):
        document = self.get_object()
        shared_with_ids = self.request.data.get('shared_with', [])
        document.shared_with.add(*shared_with_ids)
        return Response('This document has been shared successfully', status.HTTP_200_OK)

class DocumentSharedWithUserView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DocumentShareUserSerializer

    def get_queryset(self): 
        document = get_object_or_404(Document, pk=self.kwargs['pk'])
        # shared_user_ids = 
        return User.objects.filter(id__in=document.shared_with.values_list('id',flat=True))

class DocumentDownloadView(generics.RetrieveAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    pagination_classes = [IsAuthenticated,]

    def get(self, request, *args, **kwargs):
        document = self.get_object()

        # check if user can download the document
        if not document.can_be_downloaded_by_user(request.user):
            return Response({'detail': 'You do not have permission to download this document.'}, status=status.HTTP_403_FORBIDDEN)

        # check file exists or not
        if not document.file:
            return Response({'detail': 'The Document does not exist'}, status=status.HTTP_404_NOT_FOUND)

        # return the file as response
        file = document.file.file
        response = FileResponse(file)
        response['Content-Disposition'] = f'attachment; filename="{document.file.name}"'
        return response
