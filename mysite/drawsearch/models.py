from django.db import models
# from django.utils import timezone
# from django.contrib.auth.models import User

# Create your models here.

class Search(models.Model):
    OldName = models.CharField(max_length=255)
    NewName = models.CharField(max_length=255, verbose_name='File Name')
    LocationNumber = models.IntegerField(default=0, verbose_name='Location Number')
    DrawingNumber = models.IntegerField(default=0, verbose_name='Drawing Number')
    ProjectTitle = models.CharField(max_length=255, verbose_name='Project Title')
    ProjectNumber = models.CharField(max_length=255, verbose_name='Project Number')
    DrawingDate = models.IntegerField(default=0, verbose_name='Year')
    SheetTitle = models.CharField(max_length=255, verbose_name='Sheet Title')
    SheetNumber = models.CharField(max_length=255, verbose_name='Sheet Number')
    Discipline = models.CharField(max_length=255)
    DrawingVersion = models.CharField(max_length=255)
    Notes = models.CharField(max_length=255)
    PhysicalLocation = models.CharField(max_length=255)
    # date_added = models.DateTimeField(default=timezone.now)
    # added_by = models.ForeignKey(User, on_delete=models.SET_NULL)
    class Meta:
        verbose_name = "Record Drawing"
        verbose_name_plural = "Record Drawings"

    def __str__(self):
            return self.NewName


