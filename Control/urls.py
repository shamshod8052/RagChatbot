from django.urls import path
from . import views
from .views import MessageView

urlpatterns = [
    path("", views.index, name="index"),
    path("ask/", views.ask, name="ask"),
    path('messages/', views.load_messages, name='load_messages'),
    path("api/message/", MessageView.as_view(), name="message"),
]
