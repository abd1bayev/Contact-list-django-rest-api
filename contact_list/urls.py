from django.urls import path
from .views import (
    ContactListApiView,
    ContactDetailApiView
)

urlpatterns = [
    path('api/', ContactListApiView.as_view(), name="apicontact1"),
    path('api/<int:todo_id>/', ContactDetailApiView.as_view(),name="apicontact2"),
]