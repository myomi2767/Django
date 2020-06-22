from django.contrib import admin
from .models import Musician, Album

# Register your models here.
class MusicianAdmin(admin.ModelAdmin):
    list_display = ['name', 'age']

class AlbumAdmin(admin.ModelAdmin):
    list_display = ['title']

admin.site.register(Musician, MusicianAdmin)
admin.site.register(Album, AlbumAdmin)

