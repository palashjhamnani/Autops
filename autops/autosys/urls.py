from django.conf.urls import patterns, url
from autosys import views


urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'about/', views.about, name='about'),
        url(r'idol/', views.idol, name='idol'),
        url(r'delete_service/', views.delete_service, name='delete_service'),
        url(r'welcome/', views.welcome, name='welcome'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
        url(r'^linuxserver/(?P<linuxserver_name_slug>[\w\-]+)/$', views.linuxserver, name='linuxserver'),
        url(r'^farm/(?P<farm_name_slug>[\w\-]+)/$', views.farm, name='farm'),
        url(r'^add_farm/$', views.add_farm, name='add_farm'),
        url(r'^enable/', views.enable, name='enable'),
        url(r'^reboot/', views.reboot, name='reboot'),
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^search/', views.search, name='search'),
        url(r'homee/', views.homee, name='homee'),
        url(r'linuxtask/', views.linuxtask, name='linuxtask'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
        url(r'^linuxserver/(?P<linuxserver_name_slug>[\w\-]+)/add_linuxoperation/$', views.add_linuxoperation, name='add_linuxoperation'),
        url(r'^farm/(?P<farm_name_slug>[\w\-]+)/add_category/$', views.add_category, name='add_category'),
        url(r'^farm/(?P<farm_name_slug>[\w\-]+)/add_linuxserver/$', views.add_linuxserver, name='add_linuxserver'),
        )