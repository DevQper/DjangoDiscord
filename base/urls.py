from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('profile/<str:pk>/', userProfile, name='profile'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutPage, name='logout'),
    path('register/', registerPage, name='register'),
    path('room/<str:pk>/', room, name='room'),
    path('room-create/', createRoom, name='room-create'),
    path('room-update/<str:pk>', updateRoom, name='room-update'),
    path('room-delete/<str:pk>', deleteRoom, name='room-delete'),
    path('message-delete/<str:pk>', deleteMessage, name='message-delete'),
    path('topic-create/', createTopic, name='topic-create'),
    path('topic-update/<str:pk>', updateRoom, name='topic-update'),
]
