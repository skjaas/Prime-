"""prime URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.sa),
    path('index/',views.index),
    path('single/',views.single),
    path('cooler/',views.cooler),
    path('signup/',views.signup),
    path('save/',views.save),
    path('login/',views.login),
    path('log/',views.log),
    path('logout/',views.logout),
    path('mypage/',views.mypage),
    path('add/',views.add),
    path('addpro',views.addpro),
    path('laptop/',views.lap),
    path('cabinet/',views.cabinet),
    path('cooling/',views.cooling),
    path('graphics/',views.graphics),
    path('headphone/',views.cheadphone),
    path('memory/',views.cmemory),
    path('monitor/',views.cmonitor),
    path('motherboard/',views.mboard),
    path('power/',views.power),
    path('processor/',views.processing),
    path('storage/',views.storing),
    path('allpro/',views.allproject),
    path('cs/<int:id>',views.cs),
    path('cab/<int:id>',views.cab),
    path('gc/<int:id>',views.gc),
    path('hp/<int:id>',views.hp),
    path('lp/<int:id>',views.lp),
    path('my/<int:id>',views.my),
    path('mr/<int:id>',views.mr),
    path('mb/<int:id>',views.mb),
    path('ps/<int:id>',views.ps),
    path('pr/<int:id>',views.pr),
    path('sr/<int:id>',views.sr),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)