from django.urls import path
from .views import message_list, index

urlpatterns = [
    path('', index, name='index'),
    path('messages/', message_list),
]

