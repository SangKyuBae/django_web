from django.contrib import admin
from polls.models import Question, Choice

#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_text']  #change fields' order
    fieldsets = [
            ('Question Statement', {'fields': ['question_text']}),
            #('Date Information', {'fields': ['pub_date']}),
            ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
            ]
    inlines = [ChoiceInline] # see with Choice model class
    list_display = ('question_text', 'pub_date') # set record lists
    list_filter = ['pub_date'] # add filter sidebar
    search_fields = ['question_text'] # add search box

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
