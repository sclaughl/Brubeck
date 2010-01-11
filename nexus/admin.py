from django.contrib import admin
from brubeck.nexus.models import Book, Patron, Checkin, Checkout, Publisher, ShelfLocation, Author

admin.site.register(Book)
admin.site.register(Patron)
admin.site.register(Checkin)
admin.site.register(Checkout)
admin.site.register(Publisher)
admin.site.register(ShelfLocation)
admin.site.register(Author)
