from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "languageInfo_app"

urlpatterns = [
        path('NewLanguageInfo/',
                views.NewLanguageInfo.as_view(),
                name='NewLanguageInfo'),
        path('LanguageInfoAPISerializer/',
                views.LanguageInfoAPISerializer.as_view(),
                name='LanguageInfoAPISerializer'),
]
