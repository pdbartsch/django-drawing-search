from django.db import models
# from django.utils import timezone
# from django.contrib.auth.models import User

# Create your models here.

class Search(models.Model):
    OldName = models.CharField(max_length=255)
    NewName = models.CharField(max_length=255)
    LocationNumber = models.IntegerField(default=0)
    DrawingNumber = models.IntegerField(default=0)
    ProjectTitle = models.CharField(max_length=255)
    ProjectNumber = models.CharField(max_length=255)
    DrawingDate = models.IntegerField(default=0)
    SheetTitle = models.CharField(max_length=255)
    SheetNumber = models.CharField(max_length=255)
    Discipline = models.CharField(max_length=255)
    DrawingVersion = models.CharField(max_length=255)
    Notes = models.CharField(max_length=255)
    PhysicalLocation = models.CharField(max_length=255)
    # date_added = models.DateTimeField(default=timezone.now)
    # added_by = models.ForeignKey(User, on_delete=models.SET_NULL)

    def __str__(self):
            return self.NewName
