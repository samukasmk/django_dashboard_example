from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.views.generic.base import TemplateView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'smkcpanel.views.home', name='home'),
    # url(r'^smkcpanel/', include('smkcpanel.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', RedirectView.as_view(url='/server/')),
    url(r'server', include('smkcpanel.dashboard.urls')),

    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
	#url('^accounts/', include('django.contrib.auth.urls')),
    #url(r'^accounts/', include('smkcpanel.allauth.urls')),
    #url(r'^accounts/profile/$', TemplateView.as_view(template_name='allauth/plain/example/profile.html')),
)
