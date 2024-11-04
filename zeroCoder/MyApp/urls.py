from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('news', views.news, name="page2"),
    path('fun', views.fun, name="fun"),
    path('table', views.table, name="table")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)