"""introduceprj URL Configuration

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
import introduceapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', introduceapp.views.실험용, name='실험용'),
    path('시간표/', introduceapp.views.시간표, name='시간표'),
    path('department/', introduceapp.views.department, name='department'),
    path('flexgrid/', introduceapp.views.flexgrid, name='flexgrid'),

]
