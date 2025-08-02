from django.shortcuts import render, redirect
from .forms import *
from django.views import View
from django.utils.timezone import now  # وارد کردن now از django.utils.timezone
from clinic.models import *
from django.contrib.auth.mixins import LoginRequiredMixin 

class CustomerRegister(LoginRequiredMixin, View):

	template_name = f'clinic/customer_register.html'
	def get(self, request):
		form = CustomerRegisterForm
		customers = Customer.objects.all()
		return render(request, self.template_name, {'form': form, 'customers':customers})
	
	def post(self, request):
		form = CustomerRegisterForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			family_name = form.cleaned_data['family_name']
			full_name = name + " " + family_name
			phone_number = form.cleaned_data['phone_number']
			birthday = form.cleaned_data['birthday']
			national_code = form.cleaned_data['national_code']
			ensurance = form.cleaned_data['ensurance']
			
			if Customer.objects.filter(national_code = national_code).first() == None:
				new_customer = Customer.objects.create(
					full_name = full_name,
					phone_number = phone_number,
					birthday = birthday,
					national_code = national_code, 
					ensurance = ensurance
				)
				return redirect(f'clinic:index')
			else:
				customers = Customer.objects.all()
				return render(request, self.template_name, {'form': form, 'message':'کاربر با این کد ملی قبلا در سامانه ثبت نام شده است.', 'customers':customers})
		customers = Customer.objects.all()
		return render(request, self.template_name, {'form': form, 'message':'اطلاعات به صورت ناقص وارد شده است.', 'customers':customers})
	
class SubmitSessionReportView(View):

	template_name = 'clinic/submit_session_report.html'

	def get(self, request, customer_id, customer_name):
		form = SessionReportForm
		reports = SessionReport.objects.filter(customer = Customer.objects.get(id=customer_id))
		return render(request, self.template_name, {'form': form, 'reports':reports})

	def post(self, request, customer_id, customer_name):
		reports = SessionReport.objects.filter(customer = Customer.objects.get(id=customer_id))
		customer = Customer.objects.get(id=customer_id)
		form = SessionReportForm(request.POST, request.FILES)
		files = request.FILES.getlist('prescription_files')
		if form.is_valid():
			session_date = form.cleaned_data['session_date']
			cost = form.cleaned_data['cost']
			if cost == None:
				cost = 0
			description = form.cleaned_data.get('description', '')
			if description == None:
				description = '-'
			files = request.FILES.getlist('prescription_files')

			# ایجاد آبجکت SessionReport به صورت دستی
			session_report = SessionReport.objects.create(
				customer=customer,
				session_date=session_date,
				description=description,
				cost=cost
			)

			for file in files:
				PrescriptionFile.objects.create(session_report=session_report, file=file)
			return render(request, self.template_name, {'form': form, 'message':'گزارش مراجعه با موفقیت ثبت شد.', 'reports':reports})

		return render(request, self.template_name, {'form': form, 'reports':reports, 'message':'اطلاعات مراجعه ناقص ثبت شده است'})
	
class SessionsView(View):
	template_name = 'clinic/sessions.html'

	def get(self, request):
		reports = SessionReport.objects.all()
		return render(request, self.template_name, {'reports':reports})

class DeleteCustomerView(LoginRequiredMixin, View):

	def get(self, request, customer_id):
		customer = Customer.objects.get(id = customer_id)
		customer.delete()
		return redirect('clinic:index')
	
class DeleteSessionRecordView(LoginRequiredMixin, View):

	def get(self, request, session_id):
		session_record = SessionReport.objects.get(id = session_id)
		session_record.delete()
		return redirect('clinic:submit_report', session_record.customer.id, session_record.customer.full_name)

class DeleteSessionAttachmentView(LoginRequiredMixin, View):

	def get(self, request, session_id, file_id):
		session = SessionReport.objects.get(id = session_id)
		attach = PrescriptionFile.objects.get(id = file_id)
		attach.delete()
		return redirect('clinic:submit_report', session.customer.id, session.customer.full_name)















