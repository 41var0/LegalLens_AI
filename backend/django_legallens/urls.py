from django.urls import path
from django.contrib.auth import views as auth_views
from .views import HomeDashboard, subir_documento, realizar_auditacion


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),

    path('', HomeDashboard.as_view(), name='home'),
    path('dashboard', HomeDashboard.as_view(), name='home'),
    path('dashboard', HomeDashboard.as_view(), name='dashboard'),

    path('subir/doc', subir_documento, name='subir_doc'),
    path('auditar/doc', realizar_auditacion, name='auditar_doc'),
]
