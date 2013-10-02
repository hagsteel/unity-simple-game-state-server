from django.conf.urls import patterns, url
from .api import SaveGameView, LoadGameView


urlpatterns = patterns('',
    url(r'^save/$', SaveGameView.as_view(), name='save_game'),
    url(r'^load/$', LoadGameView.as_view(), name='load_game'),
)
