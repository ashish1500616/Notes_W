from django.contrib import admin
# Register your models here.
from .models import Note,Tag

class NoteAdmin(admin.ModelAdmin):
    class Meta:
        model = Note

admin.site.register(Note,NoteAdmin)
admin.site.register(Tag)