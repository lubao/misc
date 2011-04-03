from polls.models import Poll
from polls.models import Choice 
from django.contrib import admin

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 1


class PollAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields':['question']}),
		('Date Information', {'fields':['pub_date'], 
							'classes':['collapse']}),
	]
	inlines = [ChoiceInline]
	list_display = ('question', 'pub_date', 'was_published_today')
	list_filter = ['pub_date']
	search_fields = ['question']
	date_hierarchy = 'pub_date'
	#fields = ['pub_date', 'question']

admin.site.register(Poll, PollAdmin)
#admin.site.register(Choice)