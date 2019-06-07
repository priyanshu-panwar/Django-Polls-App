from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('topic', 'question_text', 'pub_date', 'date_valid')
    list_filter = ['pub_date']
    search_fields = ['topic']
    fieldsets = [
        (None, {'fields': ['topic', 'question_text']}),
        ('Date Information', {'fields': ['pub_date', 'date_valid'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)