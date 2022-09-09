from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
  
    path("", views.index, name="home"),
    path("about", views.about, name="about"),
    path("services", views.servieces, name="services"),
    path("contact", views.contact, name="contact"),
    path("register", views.register, name="register"),
    path("userdetails", views.userdetails, name="userdetails"),
    path("deletuser", views.deletuser, name="deletuser"),

    # path('admin/', admin.site.urls),

]
