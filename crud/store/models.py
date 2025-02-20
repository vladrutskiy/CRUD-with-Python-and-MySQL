from django.db import models

# Create your models here.
# Connecting existing empty Table SalesPersons
class SalesPersons(models.Model):
    First_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)
    City = models.CharField(max_length=30)
    Sales = models.CharField(max_length=30)

#  Showing desired columns
    def __str__(self):
        return (f"{self.First_Name} {self.Last_Name} {self.City} {self.Sales} ")
    
# telling not to create a new grid but connect to the existing one
    class Meta:
        db_table = 'SalesPersons'  # Map to the existing table
        managed = False  # Tell Django not to manage this table


# Connecting not empty Album table
class Album(models.Model):
    AlbumId = models.SmallIntegerField(primary_key=True)
    Title = models.CharField(max_length=35)
    ArtistId = models.SmallIntegerField()
    

#  Showing desired columns
    def __str__(self):
        return (f"{self.AlbumId} {self.Title} {self.ArtistId} ")
    
# telling not to create a new grid but connect to the existing one
    class Meta:
        db_table = 'Album'  # Map to the existing table
        managed = False  # Tell Django not to manage this table        


# Connecting not empty Track table
class Track(models.Model):
    
    TrackId = models.SmallIntegerField(primary_key=True)
    Name = models.CharField(max_length=24)
    AlbumId = models.SmallIntegerField()
    MediaTypeId = models.SmallIntegerField()
    GenreId = models.SmallIntegerField()
    Composer = models.CharField(max_length=35)
    Milliseconds  = models.CharField(max_length=7)
    Bytes = models.BigIntegerField()
    UnitPrice = models.DecimalField(max_digits=10, decimal_places=2)

#  Showing desired cpolumns
    def __str__(self):
        return (f"{self.TrackId} {self.Name} {self.AlbumId} {self.MediaTypeId} {self.GenreId} {self.Composer} {self.Milliseconds} {self.UnitPrice} ")
    
# telling not to create a new grid but connect to the existing one
    class Meta:
        db_table = 'Track'  # Map to the existing table
        managed = False  # Tell Django not to manage this table


# Connecting not empty Artist table
class Artist(models.Model):
    ArtistId = models.SmallIntegerField(primary_key=True)
    Name = models.CharField(max_length=22)
    
    

#  Showing desired columns
    def __str__(self):
        return (f"{self.ArtistId} {self.Name} ")
    
# telling not to create a new grid but connect to the existing one
    class Meta:
        db_table = 'Artist'  # Map to the existing table
        managed = False  # Tell Django not to manage this table      


# Connecting not empty Customer table
class Customer(models.Model):
    CustomerId = models.SmallIntegerField(primary_key=True)
    FirstName = models.CharField(max_length=9)
    LastName = models.CharField(max_length=12)
    Company = models.CharField(max_length=48)
    Address = models.CharField(max_length=40)
    City = models.CharField(max_length=19)
    State = models.CharField(max_length=6)
    Country = models.CharField(max_length=14)
    PostalCode = models.CharField(max_length=10)
    Phone = models.CharField(max_length=19)
    Fax = models.CharField(max_length=18)
    Email = models.CharField(max_length=29)
    SupportRepId = models.SmallIntegerField()
    

#  Showing desired columns
    def __str__(self):
        return (f"{self.CustomerId} {self.FirstName} {self.LastName} {self.Company} {self.Address} {self.City} {self.State} {self.Country} {self.PostalCode} {self.Phone} {self.Fax} {self.Email} {self.SupportRepId} ")
    
# telling not to create a new grid but connect to the existing one
    class Meta:
        db_table = 'Customer'  # Map to the existing table
        managed = False  # Tell Django not to manage this table      


# Connecting not empty Employee table
class Employee(models.Model):
    EmployeeId = models.SmallIntegerField(primary_key=True)
    FirstName = models.CharField(max_length=8)
    LastName = models.CharField(max_length=8)
    Title = models.CharField(max_length=19)
    ReportsTo = models.CharField(max_length=1)
    BirthDate = models.DateField(max_length=10)
    HireDate = models.DateField(max_length=10)
    Address = models.CharField(max_length=27)
    City = models.CharField(max_length=10)
    State = models.CharField(max_length=2)
    Country = models.CharField(max_length=6)
    PostalCode = models.CharField(max_length=7)
    Phone = models.CharField(max_length=17)
    Fax = models.CharField(max_length=17)
    Email = models.CharField(max_length=24)
    

#  Showing desired columns
    def __str__(self):
        return (f"{self.EmployeeId} {self.FirstName} {self.LastName} {self.Title} {self.ReportsTo} {self.BirthDate} {self.HireDate} {self.Address} {self.City} {self.State} {self.Country} {self.PostalCode} {self.Phone} {self.Fax} {self.Email} ")
    
# telling not to create a new grid but connect to the existing one
    class Meta:
        db_table = 'Employee'  # Map to the existing table
        managed = False  # Tell Django not to manage this table     


# Connecting not empty Genre table
class Genre(models.Model):
    GenreId = models.SmallIntegerField(primary_key=True)
    Name = models.CharField(max_length=18)
    
    

#  Showing desired columns
    def __str__(self):
        return (f"{self.GenreId} {self.Name}  ")
    
# telling not to create a new grid but connect to the existing one
    class Meta:
        db_table = 'Genre'  # Map to the existing table
        managed = False  # Tell Django not to manage this table        


# Connecting not empty Invoice table
class Invoice(models.Model):
    InvoiceId = models.SmallIntegerField(primary_key=True)
    CustomerId = models.SmallIntegerField()
    InvoiceDate = models.DateField(max_length=10)
    BillingAddress = models.CharField(max_length=40)
    BillingCity = models.CharField(max_length=19)
    BillingState = models.CharField(max_length=6)
    BillingCountry = models.CharField(max_length=14)
    BillingPostalCode = models.CharField(max_length=10)
    Total = models.DecimalField(max_digits=6, decimal_places=2)
    
    
#  Showing desired columns
    def __str__(self):
        return (f"{self.InvoiceId} {self.CustomerId} {self.InvoiceDate} {self.BillingAddress} {self.BillingCity} {self.BillingState} {self.BillingCountry} {self.BillingPostalCode} {self.Total} ")
    
# telling not to create a new grid but connect to the existing one
    class Meta:
        db_table = 'Invoice'  # Map to the existing table
        managed = False  # Tell Django not to manage this table     


# Connecting not empty InvoiceLine table
class InvoiceLine(models.Model):
    InvoiceLineId = models.SmallIntegerField(primary_key=True)
    InvoiceId = models.SmallIntegerField()
    TrackId = models.SmallIntegerField()
    UnitPrice = models.DecimalField(max_digits=3, decimal_places=2)
    Quantity = models.IntegerField()
    
    
#  Showing desired columns
    def __str__(self):
        return (f"{self.InvoiceLineId} {self.InvoiceId} {self.TrackId} {self.UnitPrice} {self.Quantity}  ")
    
# telling not to create a new grid but connect to the existing one
    class Meta:
        db_table = 'InvoiceLine'  # Map to the existing table
        managed = False  # Tell Django not to manage this table 


# Connecting not empty MediaType table
class MediaType(models.Model):
    MediaTypeId = models.SmallIntegerField(primary_key=True)
    Name = models.CharField(max_length=27)
    
    

#  Showing desired columns
    def __str__(self):
        return (f"{self.MediaTypeId} {self.Name}  ")
    
# telling not to create a new grid but connect to the existing one
    class Meta:
        db_table = 'MediaType'  # Map to the existing table
        managed = False  # Tell Django not to manage this table  


# Connecting not empty Payment table
class Payment(models.Model):
    Loan_number = models.IntegerField(primary_key=True)
    Payment_number = models.IntegerField()
    Payment_date = models.DateField(max_length=10)
    Payment_amount = models.DecimalField(max_digits=6, decimal_places=2)
    

#  Showing desired columns
    def __str__(self):
        return (f"{self.Loan_number} {self.Payment_number} {self.Payment_date} {self.Payment_amount}")
    
# telling not to create a new grid but connect to the existing one
    class Meta:
        db_table = 'Payment'  # Map to the existing table
        managed = False  # Tell Django not to manage this table   


# Connecting not empty Persons table
class Persons(models.Model):
    PersonID = models.SmallIntegerField(primary_key=True)
    FirstName = models.CharField(max_length=10)
    LastName = models.CharField(max_length=10)
    Address = models.CharField(max_length=27) 
    City = models.CharField(max_length=10) 
    
    

#  Showing desired columns
    def __str__(self):
        return (f"{self.PersonID} {self.FirstName} {self.LastName} {self.Address} {self.City} ")
    
# telling not to create a new grid but connect to the existing one
    class Meta:
        db_table = 'Persons'  # Map to the existing table
        managed = False  # Tell Django not to manage this table  


# Connecting not empty Playlist table
class Playlist(models.Model):
    PlaylistId = models.SmallIntegerField(primary_key=True)
    Name = models.CharField(max_length=26)
    
    

#  Showing desired columns
    def __str__(self):
        return (f"{self.PlaylistId} {self.Name}  ")
    
# telling not to create a new grid but connect to the existing one
    class Meta:
        db_table = 'Playlist'  # Map to the existing table
        managed = False  # Tell Django not to manage this table      


# Connecting not empty PlaylistTrack table
class PlaylistTrack(models.Model):
    PlaylistId = models.SmallIntegerField(primary_key=True)
    TrackId = models.SmallIntegerField()
    
    

#  Showing desired columns
    def __str__(self):
        return (f"{self.PlaylistId} {self.TrackId}  ")
    
# telling not to create a new grid but connect to the existing one
    class Meta:
        db_table = 'PlaylistTrack'  # Map to the existing table
        managed = False  # Tell Django not to manage this table    


