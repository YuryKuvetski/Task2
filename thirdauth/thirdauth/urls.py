from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^$', 'thirdauth.views.home', name='home'),
	url('', include('social.apps.django_app.urls', namespace='social')),
	url('', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^admin/', admin.site.urls),
]
