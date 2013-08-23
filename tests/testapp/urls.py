from django.conf.urls import patterns, url
from .views import SecureView, UnsecureView


urlpatterns = patterns('',
    url(r'^/page/secure/$', SecureView.as_view(), {'SSL': True}, name='secure_page'),
    url(r'^/page/unsecure/$', UnsecureView.as_view(), {'SSL': False}, name='unsecure_page'),
    url(r'^/page/default/$', UnsecureView.as_view(), name='default_page'),
)
