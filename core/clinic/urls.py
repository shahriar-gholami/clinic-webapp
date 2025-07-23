from django.urls import path, include
from clinic import views
from django.apps import apps

current_app_name = apps.get_containing_app_config(__name__).name



app_name = f"{current_app_name}"

urlpatterns = [
    
    path('', views.CustomerRegister.as_view(), name='index'),
    path('submit-report/<int:customer_id>/<str:customer_name>/', views.SubmitSessionReportView.as_view(), name='submit_report'),
    path('sessions/', views.SessionsView.as_view(), name='sessions'),
    path('delete-customer/<int:customer_id>/', views.DeleteCustomerView.as_view(), name='delete_customer'),
   ]