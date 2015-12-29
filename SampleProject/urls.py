"""SampleProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, patterns
from django.contrib import admin

from SampleProject.views import hello, current_datetime , current_datetime_offset, current_datetime_template, current_datetime_template_sortcut
from books.views import search_form, search
from contact.views import contact, thanks, contact_adv
from financeManager.views import auth, addPolicy , table_dynamic, deletePolicy, updatePolicy,\
    Register, Profile, sendEmail

'''
urlpatterns = ['',
    url(r'^hello/$', hello),
    url(r'^admin/', admin.site.urls),
    url(r'^time/$',current_datetime),
    url(r'^timeoffset/(\d+)$',current_datetime_offset),
    url(r'^time_template/$',current_datetime_template),
    url(r'^time_template_sort/$',current_datetime_template_sortcut),
    url(r'^search_form/$',search_form),
    url(r'^search/$',search),
    url(r'^contact/$',contact),
    url(r'^thanks/$',thanks),
    url(r'^contact-adv/$',contact_adv),
    
    
    url(r'^login/$',auth),
    url(r'^logout/$',logout),
    url(r'^login/home/$',addPolicy),
    url(r'^add/$',addPolicy),
    url(r'^home/policy/delete/$',deletePolicy),
    url(r'^home/policy/update/$',updatePolicy),

    url(r'^table_dynamic/$',table_dynamic),
]
'''
urlpatterns = patterns('',
    url(r'^hello/$', hello),
    url(r'^admin/', admin.site.urls),
    url(r'^time/$',current_datetime),
    url(r'^timeoffset/(\d+)$',current_datetime_offset),
    url(r'^time_template/$',current_datetime_template),
    url(r'^time_template_sort/$',current_datetime_template_sortcut),
    url(r'^search_form/$',search_form),
    url(r'^search/$',search),
    url(r'^contact/$',contact),
    url(r'^thanks/$',thanks),
    url(r'^contact-adv/$',contact_adv),
     url(r'^mail/$',sendEmail),
    
    url(r'^register/$', Register.as_view()),
    url(r'^login/$',auth),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/login'}),
    url(r'^home/$',addPolicy),
    url(r'^add/$',addPolicy),
    url(r'^profile/(\d)$',Profile.as_view()),
    #url(r'^account/reset_password_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView.as_view(),name='reset_password_confirm'),
    # PS: url above is going to used for next section of implementation.
    #url(r'^account/reset_password', ResetPasswordRequestView.as_view(), name="reset_password"),

    
    url(r'^user/password/reset/$', 
        'django.contrib.auth.views.password_reset', 
        {'post_reset_redirect' : '/user/password/reset/done/'},
        name="password_reset"),
    url(r'^user/password/reset/done/$',
        'django.contrib.auth.views.password_reset_done'),
    url(r'^user/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 
        'django.contrib.auth.views.password_reset_confirm', 
        {'post_reset_redirect' : '/user/password/done/'}),
    url(r'^user/password/done/$', 
        'django.contrib.auth.views.password_reset_complete'),
    url(r'^user/password/reset/confirm/$', 
             'django.contrib.auth.views.password_reset_confirm'),
    url(r'^user/password/reset/complete/$', 
             'django.contrib.auth.views.password_reset_complete'),

    url(r'^table_dynamic/$',table_dynamic),
    
) 
