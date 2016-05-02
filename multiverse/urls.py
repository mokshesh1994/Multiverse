from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.story_list, name='home'),
    url(r'^similarity/$', views.similarity, name='similarity'),
    #url(r'^up_db_fm_fl$', views.update_db_from_file, name='up_db_fm_fl')
]
