from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('registration.views',
    url(r'login/$', 'login_page'),
#    url(r'logout/$', 'logout'),
#    url(r'verify/$', 'verify'),
#    url(r'profile/$', 'edit_profile')
)