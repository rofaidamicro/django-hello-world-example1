from django.urls import path
from . import views

urlpatterns = [
    path('text/', views.text_response, name='text_response'),
    path('html/', views.html_response, name='html_response'),
    path('json/', views.json_response, name='json_response'),
    path('stream/', views.stream_response, name='stream_response'),
    path('textfile/', views.text_file_response, name='text_file_response'),
    path('image/', views.image_response, name='image_response'),
    path('pdf/', views.pdf_response, name='pdf_response'),
    path('video/', views.video_response, name='video_response'),
    path('csv/', views.csv_response, name='csv_response'),
    path('xml/', views.xml_response, name='xml_response'),
]