from __future__ import unicode_literals

from django.db import models
from department.models import department_data
import hashlib
# Create your models here.
class teachers_data(models.Model):
	id=models.CharField(max_length=120,blank=False,null=False,primary_key=True)
	otp=models.CharField(max_length=120,blank=False,null=True)
	name=models.CharField(max_length=120,blank=False,null=False)
	department= models.ForeignKey(department_data,to_field='id')
	modified= models.DateTimeField(auto_now=True,auto_now_add=False)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)
	mobile=models.CharField(max_length=120,blank=False,null=True)
	profile_image=models.ImageField(upload_to="profile",default="profile/people.png")
	email=models.CharField(max_length=120,blank=False,null=True)
	fcm=models.CharField(max_length=120,blank=False,null=True)
	def __unicode__(self):
		return str(self.name)