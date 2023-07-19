from django.db import models
from account.models import User
from personal_document_ms.base import TimeStamp
from .utils import validate_file, get_file_format

# Create your models here.
class Document(TimeStamp):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="document_owner")
    shared_with = models.ManyToManyField(User, related_name='shared_documents')
    title = models.CharField(max_length=100)
    file_format = models.CharField(max_length=50)
    description = models.TextField()
    file = models.FileField(upload_to="documents", validators=[validate_file])

    def save(self, *args, **kwargs):
        self.file_format = get_file_format(self.file)
        super(Document, self).save(*args, **kwargs)
    
    def can_be_downloaded_by_user(self, user):
        if user.is_superuser:
            return True
        elif self.owner == user or self.shared_with.filter(pk=user.pk).exists():
            return True
        return False
