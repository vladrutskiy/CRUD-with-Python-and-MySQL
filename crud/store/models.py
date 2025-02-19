from django.db import models

# Create your models here.
# Connecting existing empty Table SalesPersons
class SalesPersons(models.Model):
    First_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)
    City = models.CharField(max_length=30)
    Sales = models.CharField(max_length=30)

#  Showing desired cpolumns
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
    

#  Showing desired cpolumns
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