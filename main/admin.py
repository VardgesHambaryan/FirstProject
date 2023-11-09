from django.contrib import admin
from .models import *


@admin.register(Blog)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    list_display_links = ('title', 'date')
    search_fields = ('title' , 'date' , 'text')

admin.site.register(HomeBG)
admin.site.register(OurService)
admin.site.register(OurGallery)
admin.site.register(AboutUS)
admin.site.register(Icons)

@admin.register(ContactUs)
class ContactUsModelAdmin(admin.ModelAdmin):
    list_display = ('id' , 'name' , 'email')
    list_display_links = ('id' , 'name' , 'email')
    search_fields = ('id' , 'name' , 'email', 'message')
