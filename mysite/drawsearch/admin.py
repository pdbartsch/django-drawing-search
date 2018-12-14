from django.contrib import admin
from .models import Search

admin.site.site_header = 'UCSB Record Drawing Administration'

class SearchAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    fieldsets = [
        ('Drawing Info', {'fields': ['NewName', 'DrawingNumber', 'ProjectTitle', 'ProjectNumber', 'DrawingDate', 'SheetTitle', 'SheetNumber', 'Discipline', 'DrawingVersion' ]}),
        # ('Another Section', {'fields': ['field1', 'field2', 'etc']}),
 

    ]    
    list_display = ('NewName', 'LocationNumber', 'DrawingNumber', 'ProjectTitle', 'SheetTitle', 'Discipline')
    list_filter = ('Discipline', 'DrawingVersion')
    # https://docs.djangoproject.com/en/2.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.search_fields
    search_fields = ('LocationNumber', 'DrawingNumber', 'ProjectTitle', 'SheetTitle')
    

admin.site.register(Search, SearchAdmin)



