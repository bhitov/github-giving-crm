from django.contrib import admin
from models import *



class ChildAdmin(admin.ModelAdmin):
    pass

admin.site.register(Child, ChildAdmin)
admin.site.register(ChildUpdate)
admin.site.register(ChildFieldUpdate)
