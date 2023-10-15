from django.contrib import admin
from django.urls import path, include

from . import views


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path('', views.index, name='profiles_index'),
    path('sentry-debug/', trigger_error),
    path('<str:username>/', views.profile, name='profile'),
]
