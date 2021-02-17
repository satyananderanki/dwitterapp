from django.contrib import admin
from .models import Dweet, Comments, Follow

admin.site.register(Dweet)
admin.site.register(Comments)
admin.site.register(Follow)


# Register your models here.
