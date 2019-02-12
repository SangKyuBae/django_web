from django.conf.urls import patterns
from some_app.views import AboutView

urlpatterns = patterns('',
        (r'^about/', AboutView.as_view()),
)
