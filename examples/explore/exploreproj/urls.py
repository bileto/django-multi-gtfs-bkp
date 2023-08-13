from django.urls import include, path, re_path
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', TemplateView.as_view(template_name="explore/home.html"),
        name='home'),
    path('', include('exploreapp.urls'))
]
