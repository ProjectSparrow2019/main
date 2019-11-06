from django.urls import path, re_path
from usuarios_ import views
from django.contrib.auth.views import LoginView , LogoutView

urlpatterns = [
    re_path(r'^$', views.index,name='index'),
    #re_path(r'^project/$', views.project, name='project'),
    #re_path(r'^about/$', views.about, name='about'),
    re_path(r'^login/$', views.login_, name='login'),
    re_path(r'^logout/$', views.logout_, name='logout'),
    re_path(r'^home/$', views.home, name='home'),
    #re_path(r'^enjoy/$', views.enjoy, name='enjoy'),
    re_path(r'^search/$',views.search,name='search')
    #re_path(r'^get_products/$',views.get_products,name='get_products')
]