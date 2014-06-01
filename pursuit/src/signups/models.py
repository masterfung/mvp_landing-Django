from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.

class SignUp(models.Model): #Sign(U)p, Django will auto space it after it encounter the 'U'
	first_name = models.CharField(max_length = 120, null = True, blank = True)
	last_name = models.CharField(max_length = 120, null = True, blank = True)
	email = models.EmailField()
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)

	def __unicode__(self): #good for input outside of the utc-8
		return smart_unicode(self.email)