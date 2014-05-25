# coding=utf-8
# Register your models here.
from django.contrib import admin
from polls.models import Choice, Poll


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


class PollAdmin(admin.ModelAdmin):
    list_display = ('question', 'pub_date', 'was_published_recently')
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question']

admin.site.register(Poll, PollAdmin)
