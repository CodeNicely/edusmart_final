from __future__ import unicode_literals

from django.db import models
from classes.models import class_data
import hashlib

# Create your models here.
class students_data(models.Model):
	name=models.CharField(max_length=120,blank=False,null=False)
	id=models.CharField(max_length=120,blank=False,null=False,primary_key=True)
	mobile=models.CharField(max_length=120,blank=False,null=True)
	email=models.CharField(max_length=120,blank=False,null=True)
	fcm=models.CharField(max_length=120,blank=True,null=True)
	otp=models.CharField(max_length=120,blank=False,null=True)
	profile_image=models.ImageField(upload_to="profile",default="profile/people.png")
	modified= models.DateTimeField(auto_now=True,auto_now_add=False)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)

	def __unicode__(self):
		return str(self.id)+' '+str(self.name)

class students_in_class_data(models.Model):
	student=models.ForeignKey(students_data,to_field='id')
	class_name=models.ForeignKey(class_data,to_field='id')
