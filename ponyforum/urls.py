from django.conf                 import settings
from django.conf.urls.defaults   import patterns, include, url
from django.contrib              import admin
from django.views.generic.simple import redirect_to

from registration                import views as registration_views


admin.autodiscover()

urlpatterns = patterns('forum.views',
    (r'^$',                                      'home'),
    (r'^reports/$',                              'reports'),
#   (r'^search/$',                               'search', name='search'),
    (r'^subscriptions/$',                        'subscriptions'),
    (r'^bookmarks/$',                            'saves_and_bookmarks',
                                                    {'object_type': 'bookmark'},
                                                    'bookmarks'),
    (r'^saves/$',                                'saves_and_bookmarks',
                                                    {'object_type': 'save'},
                                                    'saves'),
    (r'^search/$',                               'search'),

#   Category
    (r'^category/add/$',                         'add'),
    (r'^category/(?P<category_id>\d+)/create/$', 'create'),
#   (r'^category/(?P<category_id>\d+)/merge/$',  'merge'),
    (r'^category/(?P<category_id>\d+)/$',        'category'),

#   Thread
    (r'^thread/(?P<thread_id>\d+)/reply/$',      'reply'),
    (r'^thread/js/$',                            'thread_js'),
    (r'^thread/(?P<thread_id>\d+)/lock/$',       'lock_thread'),
    (r'^thread/(?P<thread_id>\d+)/sticky/$',     'sticky_thread'),
    (r'^thread/(?P<thread_id>\d+)/merge/$',      'merge_thread'),
    (r'^thread/(?P<thread_id>\d+)/move/$',       'move_thread'),
    (r'^thread/(?P<thread_id>\d+)/moderate/$',   'moderate_thread'),
    (r'^thread/(?P<object_id>\d+)/report/$',     'report',
                                                    {'object_type': 'thread'},
                                                    'report_thread'),
    (r'^thread/(?P<object_id>\d+)/remove/$',     'remove',
                                                    {'object_type': 'thread'},
                                                    'remove_thread'),
    (r'^thread/(?P<thread_id>\d+)/$',            'thread',
                                                    {'author_id': 'Everyone'}),
	(r'^thread/(?P<thread_id>\d+)/author/(?P<author_id>\d+)/$', 'thread'),

#   Post
    (r'^post/(?P<post_id>\d+)/edit/$',           'edit'),
    (r'^post/(?P<object_id>\d+)/report/$',       'report',
                                                    {'object_type': 'post'},
                                                    'report_post'),
    (r'^post/(?P<object_id>\d+)/remove/$',       'remove',
                                                    {'object_type': 'post'},
                                                    'remove_post'),
    (r'^post/(?P<post_id>\d+)/$',                'post'),

#   User
    (r'^user/js/$',                              'user_js'),
    (r'^user/(?P<user_id>\d+)/threads/$',        'user_content',
                                                     {'object_type': 'thread'},
                                                     'user_threads'),
    (r'^user/(?P<user_id>\d+)/posts/$',          'user_content',
                                                     {'object_type': 'post'},
                                                     'user_posts'),
    (r'^user/(?P<user_id>\d+)/$',                'user'),
)

#   Accounts
urlpatterns += patterns('',
    url(r'^' + getattr(settings, 'LOGIN_URL'[1:],
                                                 'accounts/login/') + '$',
                                                 'django.contrib.auth.views.login',
                                                  name='login'),
    url(r'^' + getattr(settings, 'LOGOUT_URL'[1:],
                                                 'accounts/logout/') + '$',
                                                 'django.contrib.auth.views.logout',
                                                {'next_page': '/'},
                                                  name='logout'),
    url(r'^' + getattr(settings, 'REGISTRATION_URL'[1:],
                                                 'accounts/register/') + '$',
                                                  registration_views.register,
                                                  name="register"),
    # (r'^accounts/settings/$',                    'settings'),
)

urlpatterns += patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/',     include(admin.site.urls)),
    url(r'^accounts/',  include('registration.urls')),
)