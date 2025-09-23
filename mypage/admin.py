from django.contrib import admin
from mypage.models import Contact 

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'number', 'created_at')
    list_filter = ('created_at',) 
    search_fields = ('name', 'email')

admin.site.register(Contact, ContactAdmin)
