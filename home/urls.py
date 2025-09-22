from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='home'),
    path('projects/', views.projects, name='projects'),
    path('blog/', views.blog, name='blog'),
    path('resume/', views.resume, name='resume'),
    path('contact/', views.contact, name='contact'),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html', redirect_authenticated_user=True, next_page='/'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]
