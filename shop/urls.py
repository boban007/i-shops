"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
import category.views as category
import products.views as products
import home.views as home

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('i18n/', include('django.conf.urls.i18n')),
    #path('', include('home.urls')),
]
urlpatterns += i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    path('', include('home.urls')),
    path('search/', home.search, name='search'),
    path('category/<category>', category.index),
    path('product/<product>', products.index),
    prefix_default_language=True,
)
