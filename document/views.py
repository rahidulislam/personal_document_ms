from django.http import HttpResponse, FileResponse, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Document
from .serializers import DocumentSerializer, DocumentShareSerializer
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


class DocumentDownloadView(generics.RetrieveAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    pagination_classes = [IsAuthenticated]

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
