from django.contrib import admin
from .models import Member, Movie

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display = ("username", "firstname", "lastname", "phone", "email")
    search_fields = ("username",)

class Movies(admin.ModelAdmin):
    list_display = ("title", "description", "source", "image_src")
    search_fields = ("title",)

admin.site.register(Member, MemberAdmin)
admin.site.register(Movie, Movies)