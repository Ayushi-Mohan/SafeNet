from django.urls import path

from . import views
urlpatterns = [
    path('',views.index, name="home"),
    path('plan_info',views.plan_info, name="plan_info"),
    path('login',views.login, name="login"),
    path('signup',views.signup, name="signup"),
]
