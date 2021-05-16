from django.contrib import admin
from api.models import Snippet

# Register your models here.

class SnippetAdmin (admin.ModelAdmin):
    pass
admin.site.register(Snippet, SnippetAdmin)