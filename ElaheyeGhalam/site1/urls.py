from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('decorsazi/', views.decorsazi, name='decorsazi'),
    path('ghorfesazi/', views.ghorfesazi, name='ghorfesazi'),
    path('kabinet_sazi/', views.kabinet_sazi, name='kabinet_sazi'),
    path('chap_va_tablighat/', views.chap_va_tablighat, name='chap_va_tablighat'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('contactus/', views.contactus, name='contactus'),
]