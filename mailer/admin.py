# mailer/admin.py
from django.contrib import admin
from .models import Person
from .models import Recipient

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')

admin.site.register(Recipient)