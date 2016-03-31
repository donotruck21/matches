from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',

	# this url pattern matches an empty string
	url(r'^$', views.index, name='index'),

	# url(r'^add/$', views.add, name='add'),

)
