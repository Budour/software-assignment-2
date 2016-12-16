from django.conf.urls import url
from . import views

urlpatterns = [

    #/blog/
    url(r'^$',views.detail),

    #/blog/12/
    url(r'^(?P<blog_id>[0-9]+)/$',views.index),

]
