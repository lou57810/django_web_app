"""merchex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bands/', views.band_list, name='band-list'),
    path('bands/<int:id>/', views.band_detail, name='band-detail'),
    path('bands/add/', views.band_create, name='band-create'),
    path('bands/<int:id>/update/', views.band_update, name='band-update'),
    path('bands/<int:id>/delete/', views.band_del, name='band-delete'),
    path('articles/', views.listing_list, name='listing-list'),
    path('articles/<int:id>/', views.listing_detail, name='listing-detail'),
    path('articles/add/', views.listing_create, name='listing-create'),
    path('articles/<int:id>/update/', views.data_update, name='data-update'),
    path('articles/<int:id>/delete/', views.listing_del, name='listing-delete'),
    path('about-us/', views.about, name='about-list'),
    path('contact-us/', views.contact, name='contact-list'),
    #url(r'^rest-auth/', include('rest_auth.urls'))

]
