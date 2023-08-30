from django.urls import path

from CollegeManagement import views

urlpatterns = [
    path('',views.base_fun),
    path('signin',views.signup_fun,name='signin'),
    path('login',views.login_fun,name='login'),
    path('home',views.home_fun,name='home'),
    path('add',views.add_fun,name='add'),
    path('display',views.display_fun,name='display'),
    path('logout',views.logout_fun,name='logout'),
    path('update /<int:id>',views.update_fun,name='update'),
    path('delete /<int:id>',views.delete_fun,name='delete'),
]