from django.conf.urls import url
from . import views

urlpatterns = [

    #/blog/
    url(r'^$',views.detail),

    #/blog/12/
    url(r'^(?P<blog_id>[0-9]+)/$',views.index),

    url(r'^all/$', views.show_all_blog),

    url(r'^all/user/(?P<userId>[0-9]+)$', views.show_all_blog_from_user),

]
