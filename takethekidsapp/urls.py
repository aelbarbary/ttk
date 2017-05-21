from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'takethekidsapp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^accounts/profile/$', view=views.index, name ='dislike_resourse')
]
