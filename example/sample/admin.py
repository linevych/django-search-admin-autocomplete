from django.contrib import admin
from search_admin_autocomplete.admin import SearchAutoCompleteAdmin
from .models import DummyModel


class DummyModelAdmin(SearchAutoCompleteAdmin):
    search_fields = ['name']


admin.site.register(DummyModel, DummyModelAdmin)
