from django.db import models
import datetime


# Create your models here.
class Poll(models.Model):
	def __unicode__(self):
		return unicode('The question is {0}'.format(self.question))

	question = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def was_published_today(self):
		return self.pub_date.date() == datetime.date.today()
	
	was_published_today.short_description = 'published today?'


class Choice(models.Model):
	def __unicode__(self):
		return unicode('The choice is {0}'.format(self.choice))
	
	poll = models.ForeignKey(Poll)
	choice = models.CharField(max_length=200)
	vote = models.IntegerField()
