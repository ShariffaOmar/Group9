from django.contrib import admin
from .models import Cart, Order,Payment


admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Payment)
