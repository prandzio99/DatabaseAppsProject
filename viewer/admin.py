from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Address)
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Tag)
admin.site.register(ReadingList)
admin.site.register(BookTag)
admin.site.register(ReadingListBook)
