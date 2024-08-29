from django.contrib import admin
from crud_app.models import PersonData

# Register your models here.

@admin.register(PersonData)
class PersonDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'qualification', 'gender']
    