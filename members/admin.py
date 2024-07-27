from django.contrib import admin
from .models import Member

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display = ("username", "firstname", "lastname", "phone", "email")
admin.site.register(Member, MemberAdmin)