from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # Examples:
    # url(r'^$', 'k9server.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += patterns('k9frontend.views',
                        url(r'^$', 'index', name='index'),
                        #url(r'^search/(?P<extension_name>\S+)/$', 'search_extension', name='search_extension'),
                        #url(r'^search/(?P<program>\w+)/$', 'search_program', name='search_program'),
                        #url(r'^top/$', 'get_top_results', name='get_top_results'),

                        )
urlpatterns += staticfiles_urlpatterns()
