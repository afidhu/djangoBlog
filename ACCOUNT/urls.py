from django.urls import path
from django.contrib.auth import views as auth_view

from.import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('deactive/<int:pk>/', views.deactive, name='deactive'),
    path('active/<int:pk>/', views.active, name='active'),
    path('approved/<int:pk>/', views.approved, name='approved'),
    path('user_delete/<int:pk>/', views.user_delete, name='user-delete'),
    path('not_approved/<int:pk>/', views.not_approved, name='not_approved'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_view.LoginView.as_view(template_name='user/login.html'), name='login'),
]
