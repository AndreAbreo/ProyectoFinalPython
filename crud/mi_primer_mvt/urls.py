"""mi_primer_mvt URL Configuration

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
from Tienda.views import (index, ComicList, 
                                ComicDetail, ComicCreate, ComicUpdate,
                                ComicDelete, SignUp, Login, Logout,
                                ProfileUpdate, MensajeCreate, MensajeDelete, MensajeList, ProfileCreate, about)

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name="index"),
    path('admin/', admin.site.urls),
    path('comic/list', ComicList.as_view(), name="comic-list"),
    path('comic/<pk>/detail', ComicDetail.as_view(), name="comic-detail"),
    path('comic/create', ComicCreate.as_view(), name="comic-create"),
    path('comic/<pk>/update', ComicUpdate.as_view(), name="comic-update"),
    path('comic/<pk>/delete', ComicDelete.as_view(), name="comic-delete"),
    path('signup/', SignUp.as_view(), name="signup"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
    path('profile/<pk>/update', ProfileUpdate.as_view(), name="profile-update"),
    path('mensaje/create', MensajeCreate.as_view(), name="mensaje-create"),
    path('mensaje/list', MensajeList.as_view(), name="mensaje-list"),
    path('mensaje/<pk>/delete', MensajeDelete.as_view(), name="mensaje-delete"),
    path('profile/create', ProfileCreate.as_view(), name="profile-create"),
    path('about', about, name="about"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)