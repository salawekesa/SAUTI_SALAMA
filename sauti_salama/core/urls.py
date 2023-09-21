from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('report_list', views.sgbv_report_list, name='report_list'),
    path('create_report', views.create_sgbv_report, name='report_list')
]

