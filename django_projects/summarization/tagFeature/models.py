from django.db import models

# Create your models here.
class Advertise(models.Model):
    marked = models.BooleanField(default = 'False')
    content = models.TextField()
    
    def __unicode__(self):
        return u'id={0} conten={1}'.format(self.id, self.content)
    
    
    class Meta:
        ordering = ['marked']
