from django.conf.urls import include, url


urlpatterns = [
    url(r'^tests/', include('testapp.urls')),
]
