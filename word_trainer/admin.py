from django.contrib import admin
from .models import Dictionary, Word
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class WordResource(resources.ModelResource):

    class Meta:
        model = Word
        fields = ('id', 'dictionary', 'word_rus', 'word_eng', 'is_trouble')


class WordAdmin(ImportExportModelAdmin):
    resource_class = WordResource


admin.site.register(Word, WordAdmin)

admin.site.register(Dictionary)
