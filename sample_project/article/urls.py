from django.conf.urls.defaults import *
from sample_project.article import views


urlpatterns = patterns('',
    url(r'^images/', include(views.file_picker.urls))
)