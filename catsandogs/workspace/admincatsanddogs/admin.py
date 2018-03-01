from django.contrib import admin
from .models import Owner, Cats, Dogs
# Register your models here.
admin.site.register(Owner)
admin.site.register(Cats)
admin.site.register(Dogs)
