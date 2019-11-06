'''from django.urls import path

from . import views
urlpatterns = [
    path('',views.index, name="home"),
    path('plan_info',views.plan_info, name="plan_info"),
    path('login',views.login, name="login"),
    path('signup',views.signup, name="signup"),
]'''

from django.conf.urls import url
from safenet import views
# SET THE NAMESPACE!
app_name = 'safenet'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^plan_info/$',views.plan_info, name="plan_info"),
    url(r'^signup/$',views.signup,name='signup'),
    url(r'^user_login/$',views.user_login,name='user_login'),
]
