from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^weibo/', include('weibo.urls', namespace='weibo')),
                       # Examples:
                       # url(r'^$', 'data_analysis.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       )
