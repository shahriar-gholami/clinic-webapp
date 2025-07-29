
from django import forms
from . models import SessionReport

class CustomerRegisterForm(forms.Form):

	name = forms.CharField()
	family_name = forms.CharField()
	phone_number = forms.CharField()
	birthday = forms.CharField(required=False)
	national_code = forms.CharField()
	ensurance = forms.CharField(required=False)

class CourseRegisterForm(forms.Form):
	title = forms.CharField()
	customer = forms.CharField()
	reserved_sessions = forms.IntegerField()
	cost_paid = forms.IntegerField()
	instructor = forms.CharField()
	date = forms.CharField()

class SelectInstructor(forms.Form):
	instructor = forms.CharField()

class InstructorDeptForm(forms.Form):
	instructore_income = forms.CharField()

class GymCosts(forms.Form): 
	description = forms.CharField()
	amount = forms.IntegerField()

class InstructorRegister(forms.Form):
	full_name = forms.CharField()
	phone_number = forms.CharField()
	national_code = forms.CharField()
	courses = forms.CharField()
	share_percent = forms.IntegerField()
	birthday = forms.CharField()
	study = forms.CharField()
	address = forms.CharField()

class CourseAdd(forms.Form):
	title = forms.CharField()

class SessionReportForm(forms.Form):
	prescription_files = forms.FileField(required=False)
	session_date = forms.CharField()
	description = forms.CharField(required = False)
	cost = forms.IntegerField(required=False)

