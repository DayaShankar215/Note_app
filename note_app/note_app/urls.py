"""
URL configuration for note_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
# filepath: c:\Users\dayas\Desktop\Django training\Daya\note_app\note_app\urls.py
from django.contrib import admin
from django.urls import path
from note.views import index, welcome, delete_note, edit_note

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome, name='welcome'),  # Welcome page as the default
    path('notes/', index, name='index'),  # Notes page
    path('delete/<int:id>/', delete_note, name="delete_note"),
    path('edit/<int:id>/', edit_note, name="edit_note"),
]