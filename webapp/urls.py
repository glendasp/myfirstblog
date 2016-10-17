__author__ = 'Glenda Pinho'


from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^results', views.results, name='results'),
    url(r'^$', views.crawler, name='crawler'),
    url(r'^about', views.about, name='about'),
]
