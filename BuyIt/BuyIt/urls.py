"""BuyIt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static
from .views import index
from products.views import (
    Product_List,
    Product_Detail,
    ProductFeaturedDetailView,
    Product_Slug_Detail,
    ProductFeaturedListView
    )

urlpatterns = [
    path('',index),
    path('admin/', admin.site.urls),
    path('products/',Product_List),
    path('featured/',ProductFeaturedListView.as_view()),
    re_path('products/(?P<pk>\d+)/',Product_Detail),
    # re_path('products/(?P<slug>[\w-]+)/',Product_Slug_Detail.as_view()),
    re_path('featured/(?P<pk>\d+)/',ProductFeaturedDetailView.as_view())
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)