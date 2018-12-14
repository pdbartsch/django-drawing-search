from django.contrib import admin
from .models import Search

admin.site.site_header = 'UCSB Record Drawing Administration'

class SearchAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    fieldsets = [
        (None,               {'fields': ['NewName']}),
        (None,               {'fields': ['LocationNumber']}),
        (None,               {'fields': ['DrawingNumber']}),
        (None,               {'fields': ['ProjectTitle']}),
        (None,               {'fields': ['ProjectNumber']}),
        (None,               {'fields': ['DrawingDate']}),
        (None,               {'fields': ['SheetTitle']}),
        (None,               {'fields': ['SheetNumber']}),
        (None,               {'fields': ['Discipline']}),
        (None,               {'fields': ['DrawingVersion']}),

    ]    
    list_display = ('NewName', 'LocationNumber', 'DrawingNumber', 'ProjectTitle', 'SheetTitle', 'Discipline')
    list_filter = ('Discipline', 'DrawingVersion')
    # https://docs.djangoproject.com/en/2.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.search_fields
    search_fields = ('LocationNumber', 'DrawingNumber', 'ProjectTitle', 'SheetTitle')
    

admin.site.register(Search, SearchAdmin)



