from django.urls import path, include
from accounts import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView

app_name = 'accounts'

urlpatterns = [
	# path('home/', TemplateView.as_view(template_name='home.html'), name='home'),
	path('signup/', views.signup.as_view(), name='signup'),
	#path('signup/', views.signup, name="signup_view"),
	#path('login/', login, {'template_name': 'accounts/login.html'}),
	#path('login/', views.login.as_view(), name='login'),
	path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
	path('menu/', views.menu, name='home'),
	path('interes/', LoginView.as_view(template_name='accounts/interes.html'), name='interes'),
	#path('signup/', views.signup, name="signup"),
	#auth_views.LoginView.as_view(template_name='accounts/login.html'),),
]