from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views 

urlpatterns = [
    path(' ', auth_views.LoginView.as_view(
        template_name="todo/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path("create/",
         views.create_todo,
         name='create_todo'),
    path("update/<int:task_id>/",
         views.update_todo,
         name="update_todo"),
]
