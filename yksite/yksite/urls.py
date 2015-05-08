import sf1config.views

from django.conf.urls import patterns, include, url
from django.contrib import admin
from sf1config.forms import SOURCE_FORM

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'yksite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'testApp.views.home'),
    url(r'^search/$', 'testApp.views.search'),
    url(r'^sf1config/sourceConfigWizard/$' , sf1config.views.SourceConfigWizard.as_view (SOURCE_FORM))
)
