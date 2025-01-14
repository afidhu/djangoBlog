from django.urls import path
from.import views

urlpatterns = [
    path('', views.dashboard, name='dashboard' ),
    path('post_detail/<int:pk>/',views.postdetail, name='post-detail' ),
    path('update_post/<int:pk>/', views.post_update, name='post-update' ),
    path('post_del<int:pk>/', views.post_delete, name='post-delete' ),

]

