from django.contrib import admin
from django.contrib import admin
from .models import *

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(User)
admin.site.register(Supplier)
admin.site.register(Cart)
admin.site.register(Comments)