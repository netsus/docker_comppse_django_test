from django.urls import path

from test import views

urlpatterns=[
    path("", views.test_view, name="test"),
]