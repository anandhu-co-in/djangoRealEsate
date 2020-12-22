from django.contrib import admin

# Register your models here.

from .models import Listing



#this callass if created and paased to register does modidfy the list display in admin panel
class ListingAdmin(admin.ModelAdmin):
    list_display=('id','title','is_published','realtor')
    list_display_links=('id','title')
    list_editable=('is_published',)
    list_filter=('realtor','is_published')
    list_per_page=25


admin.site.register(Listing,ListingAdmin)