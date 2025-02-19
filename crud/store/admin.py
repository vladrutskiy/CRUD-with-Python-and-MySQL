from django.contrib import admin
from .models import SalesPersons, Track, Album


# Register your models here.
@admin.register(SalesPersons)
class SalesPersonsAdmin(admin.ModelAdmin):
    list_display = ('First_Name', 'Last_Name', 'City', 'Sales')

@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('TrackId', 'Name', 'AlbumId', 'MediaTypeId', 'GenreId', 'Composer', 'Milliseconds', 'UnitPrice')

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('AlbumId', 'Title', 'ArtistId')    