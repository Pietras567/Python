"""
URL configuration for Zadanie3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home_view'),
    path('api/data', views.KlasaListCreateAPIView.as_view(), name='klasa-list-create'),
    path('api/data/<int:pk>', views.KlasaDetailAPIView.as_view(), name='klasa-detail'),
    path('delete/<int:pk>', views.delete_record, name='delete_record'),
    path('add', views.add_view, name='add_view'),
    path('api/data/example', views.generate_example_data, name='generate_example_data'),
]
