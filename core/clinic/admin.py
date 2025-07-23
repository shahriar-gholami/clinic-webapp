from django.contrib import admin
from.models import *


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'create_date', 'ensurance')
    search_fields = ('full_name', 'phone_number', 'national_code')
    list_filter = ('ensurance', 'create_date')

class PrescriptionFileInline(admin.TabularInline):  # یا StackedInline برای ظاهر ستونی
    model = PrescriptionFile
    extra = 1  # چند فرم خالی برای افزودن فایل جدید نمایش داده بشه

class SessionReportAdmin(admin.ModelAdmin):
    list_display = ['customer', 'session_date']
    inlines = [PrescriptionFileInline]

admin.site.register(SessionReport, SessionReportAdmin)
