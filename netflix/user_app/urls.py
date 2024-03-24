from django.contrib import admin
from django.urls import path
from .views import *

#config
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('register',register_page,name="page-register"),
    path('login',login_page,name="page-login"),
    path('browse/profile',select_profile,name="page-select-profile"),
    path('browse/profiles/<profileId>/update',updateProfile,name="page-update-profile"),
    path('browse/profiles/<profileId>/delete',delete_profile,name="page-delete-profile")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
