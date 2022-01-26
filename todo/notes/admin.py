from django.contrib import admin

from notes.models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("title", "text", "created_at")
    fields = ("title", "text")
    readonly_fields = ("created_at",)
    search_fields = ("title", "text")