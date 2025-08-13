from django.urls import path
from django.conf.urls.i18n import set_language

from . import views  # Make sure to import views here

urlpatterns = [

    path('', views.welcome_view, name='welcome'),
    path('certificates/', views.all_certificates, name='all_certificates'),
    path('projects/', views.all_signature_projects, name='all_signature_projects'),


    # path("login/", views.user_login, name="login"),
    # path('about/', views.about_view, name='about'),  # Ensure the path is registered
    # path("logout/", views.user_logout, name="logout"),


    
    # path('contact/', views.contact, name='contact'),  # Ensure the path is registered
    # path('signup/', views.signup_view, name='signup'),
    # path('register/', views.register, name='register'),





]
