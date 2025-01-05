from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Main page
    path('submit/', views.submit_message, name='submit_message'),  # Submit message
    path('get/<str:sender_name>/', views.get_messages, name='get_messages'),  # Get messages
]
