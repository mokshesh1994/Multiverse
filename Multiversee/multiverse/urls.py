from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.story_list, name='home'),
    #url(r'^similarity/$', views.similarity, name='similarity'),
    #url(r'^up_db_fm_fl$', views.update_db_from_file, name='up_db_fm_fl')
    url(r'^science_fiction$', views.science_fiction, name='science_fiction'),
    url(r'^horror$', views.Horror, name='horror'),
    url(r'^romance$', views.Romance, name='romance'),
    url(r'^mystery_suspence$', views.mystery_suspence, name='mystery_suspence'),
    url(r'^realistic_fiction$', views.realistic_fiction, name='realistic_fiction'),
    url(r'^historical_fiction$', views.historical_fiction, name='historical_fiction'),
    url(r'^action_adventure$', views.action_adventure, name='action_adventure'),
    url(r'^humor$', views.Humor, name='humor'),
    url(r'^speculative_fiction$', views.speculative_fiction, name='speculative_fiction'),
    url(r'^thriller$', views.Thriller, name='thriller'),
    url(r'^urban$', views.Urban, name='urban'),
    url(r'^non_fiction$', views.non_fiction, name='non_fiction'),
    url(r'^about$', views.about_page, name='about'),
    url(r'^contact$', views.contact_page, name='contact')
    


]
