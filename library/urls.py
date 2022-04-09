"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from books.views import get_hello, get_uuids_a, get_uuids_b, get_image, get_button

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_hello),
    path('uuid-a', get_uuids_a),
    path('uuid-b', get_uuids_b),
    path('image', get_image),
    path('button', get_button),

]