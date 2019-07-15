from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Restaurant,Review,Comment,Category

admin.site.register(Review)


admin.site.register(Comment)

admin.site.register(Restaurant)

admin.site.register(Category)

