from django.contrib import admin
from phonebook.models import Phonebook

# # Register your models here.
# admin.site.register(Phonebook)


class phonebookView(admin.ModelAdmin):
    list_display=('fname','lname','phone','address','email','birthday') 

# Register your models here.
admin.site.register(Phonebook,phonebookView)