from django.urls import path, include
from personal import views

urlpatterns = [
    path("", views.home, name="homepage"),
    path("about/", views.about, name="aboutpage"),
    path("contact/", views.contact, name="contactpage"),
]
