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
                        url(r'^login/$', 'login', name='login'),
                        url(r'^message/new/$', 'add_message', name='add_message'),
                        url(r'home/$', 'home', name='home'),
                        url(r'home/(?P<username>\w+)$', 'get_user_details', name='get_user_details'),
                        url(r'user/(?P<username>\w+)/chart$', 'get_user_chart', name='get_user_chart'),
                        url(r'user/(?P<username>\w+)/analysis$', 'get_user_analysis', name='get_user_analysis'),
                        #url(r'^search/(?P<program>\w+)/$', 'search_program', name='search_program'),
                        #url(r'^top/$', 'get_top_results', name='get_top_results'),

                        )
urlpatterns += staticfiles_urlpatterns()
