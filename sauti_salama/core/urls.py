from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('report_list', views.sgbv_report_list, name='report_list'),
    path('create_report', views.create_sgbv_report, name='report_list'),
    path('single_report/<pk>/', views.single_report, name="single_listing"),
    path('user_profile', views.user_profile, name='user_profile'),
    # path('signup/', views.signup, name='signup'),
    # path('login/', views.login, name='login')
]