from django.contrib import admin

from fuzzy_tracker.models import Kitten


@admin.register(Kitten)
class KittenAdmin(admin.ModelAdmin):
    list_display = ("name", "age")
    list_filter = ("age",)
    search_fields = ("name", "age")
