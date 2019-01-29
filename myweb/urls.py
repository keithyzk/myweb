from django.conf.urls import include, url
from django.contrib import admin
import blog.views as bv
urlpatterns = [
    # Examples:
    # url(r'^$', 'myweb.views.home', name='home'),
    url(r'^blog/', include('blog.urls')),
    # url(r'^blog/', include('blog.views')),
    url(r'^admin/', admin.site.urls),
    # url(r'^index/', bv.index),
    url(r'^index/', include('blog.urls', namespace='blog'))
]
