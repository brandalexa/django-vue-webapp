"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *


urlpatterns = [
    # API entry points should be defined here
    path('events.json', get_all_events, name='all events'),
    path('new-event/', create_event, name='create new event'),
    path('edit-event/', edit_event, name="edit event"),
    path('event/<int:event_id>/', get_event, name="get event"),
    path('delete-event/', delete_event, name="delete event")
]
