from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.conf.urls.static import static
from simpleFirstApp import views, apiViews
from simpleDjangoProject import settings
from simpleFirstApp.ViewClassForm import ViewClassForm

urlpatterns = [
    path('',include('simpleFirstApp.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
