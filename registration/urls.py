from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('registration.views',
    url(r'login/$', 'login_page'),
    url(r'logout/$', 'logout_page'),
    url(r'register/$', 'register'),
#    url(r'verify/$', 'verify'),
#    url(r'profile/$', 'edit_profile')
)