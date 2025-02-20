from django.contrib import admin
from .models import SalesPersons, Track, Album, Artist, Customer, Employee, Genre, Invoice, InvoiceLine, MediaType, Payment, Persons, Playlist, PlaylistTrack


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

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('ArtistId', 'Name')       

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('CustomerId', 'FirstName', 'LastName', 'Company', 'Address', 'City', 'State', 'Country', 'PostalCode', 'Phone', 'Fax', 'Email', 'SupportRepId')     

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('EmployeeId', 'FirstName', 'LastName', 'Title', 'ReportsTo', 'BirthDate', 'HireDate', 'Address', 'City', 'State', 'Country', 'PostalCode', 'Phone', 'Fax', 'Email')    

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('GenreId', 'Name')     


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('InvoiceId', 'CustomerId', 'InvoiceDate', 'BillingAddress', 'BillingCity', 'BillingState', 'BillingCountry', 'BillingPostalCode', 'Total' )    


@admin.register(InvoiceLine)
class InvoiceLineAdmin(admin.ModelAdmin):
    list_display = ('InvoiceLineId', 'InvoiceId', 'TrackId', 'UnitPrice', 'Quantity')


@admin.register(MediaType)
class MediaTypeAdmin(admin.ModelAdmin):
    list_display = ('MediaTypeId', 'Name')   


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('Loan_number', 'Payment_number', 'Payment_date', 'Payment_amount') 



@admin.register(Persons)
class PersonsAdmin(admin.ModelAdmin):
    list_display = ('PersonID', 'FirstName', 'LastName', 'Address', 'City')  



@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('PlaylistId', 'Name')  



@admin.register(PlaylistTrack)
class PlaylistTrackAdmin(admin.ModelAdmin):
    list_display = ('PlaylistId', 'TrackId')     