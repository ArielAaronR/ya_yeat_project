from django.conf.urls import url
from . import views

urlpatterns = [
    # renders template
    url(r'^$', views.index),
    # process random location
    url(r'^rng$', views.rng),
    # renders result template
    url(r'^result$', views.result),
    # reset session
    url(r'^reset$', views.reset),

]
