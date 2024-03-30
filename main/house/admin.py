from django.contrib import admin
from .models import House


class HouseAdmin(admin.ModelAdmin):
    read_only_fields = [
        "id",
        "created_on",
    ]


# Register your models here.
admin.site.register(House, HouseAdmin)
