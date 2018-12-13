from django.db import models

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

    def __str__(self):
            return self.NewName
