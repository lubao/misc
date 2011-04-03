from django.db import models
FREQ_CHOICE = (
		('1','Hourly'),
		('2','Two Hourly'),
		('3','Three Hourly'),
		('4','Four Hourly'),
		('5','Five Hourly'),
		('6','Six Hourly'),
		('7','Seven Hourly'),
		('8','Eight Hourly'),
		('9','Nine Hourly'),
		('10','Ten Hourly'),
		('11','Eleven Hourly'),
		('12','Twelve Hourly'),
	)
# Create your models here.
class reminder(models.Model):
	
	def __unicode__(self):
		return 'Sending {0} reminder to {1} every {2}.'.format(
						self.medication, self.phone,self.freq)
	
	phone = models.CharField(max_length=20)
	freq = models.CharField(max_length=2, choices=FREQ_CHOICE)
	medication = models.CharField(max_length=100)
