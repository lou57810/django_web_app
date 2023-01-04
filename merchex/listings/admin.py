from django.contrib import admin
from listings.models import Band
from listings.models import Listing


# Register your models here.

# class BandAdmin(admin.ModelAdmin):
class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre', 'biography', 'year_formed', 'active', 'official_homepage')


class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'sold', 'year_formed', 'type', 'band')


# admin.site.register(Band)

admin.site.register(Band, BandAdmin)

admin.site.register(Listing, ListingAdmin)


