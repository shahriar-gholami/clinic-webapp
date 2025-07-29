from django.db import models
from django.utils.translation import gettext_lazy as _
from khayyam import JalaliDatetime
from django.utils.timezone import now
from django.db.models import Sum
from accounts.models import *



class Customer(models.Model):
	full_name = models.CharField(max_length=30)
	create_date = models.DateTimeField(default=now)  # مقدار پیش‌فرض به‌جای auto_now_add
	birthday = models.CharField(max_length=250, null=True, blank=True)
	ensurance = models.CharField(max_length=255, null=True, blank=True)
	national_code = models.CharField(max_length=250, unique=True, null=True, blank=True)
	phone_number = models.CharField(max_length=250)

	
	
	def get_total_payments(self):
		total = 0
		sessions = SessionReport.objects.filter(customer=self)
		if sessions == None:
			return total
		else:
			for session in sessions:
				total = total + session.cost
			return total
		
	def get_last_session_date(self):
		last_session = SessionReport.objects.filter(customer=self).last()
		if last_session != None:
			return last_session.session_date
		else:
			return '-'

	@property
	def register_date(self):
		return JalaliDatetime(self.create_date).strftime('%Y/%m/%d')
	
	def __str__(self):
		return f'{self.full_name}'
	
class SessionReport(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	session_date = models.CharField(max_length=255)
	description = models.TextField(null=True, blank=True)
	cost = models.IntegerField(default=0, null=True, blank=True)

	def get_attachments(self):
		return PrescriptionFile.objects.filter(session_report = self)

class PrescriptionFile(models.Model):
	session_report = models.ForeignKey(SessionReport, on_delete=models.CASCADE, related_name='prescriptions')
	file = models.FileField(upload_to='media/')


