"""BaliSimulation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views 1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home') Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from bali import views


urlpatterns = [
    url(r'^$',views.index,name="index"),
    url(r'^faq/$',views.faq,name="faq"),
    url(r'^intro/$',views.intro,name="intro"),
    url(r'^operation/$',views.operation,name="operation"),

    url(r'^readBalise/$',views.readBalise,name="readBalise"),
    url(r'^readBalise/readTele/$',views.readTele,name="readBalise/readTele"),
    url(r'^readBalise/compareTele/$',views.compareTele,name="readBalise/compareTele"),

    url(r'^writeBalise/$',views.writeBalise,name="writeBalise"),
    url(r'^writeBalise/writeTele/$',views.writeTele,name="writeBalise/writeTele"),

    url(r'^writeLEU/$',views.writeLEU,name="writeLEU"),
    url(r'^writeLEU/writeTE1/$',views.writeTE1,name="writeLEU/writeTE1"),
    url(r'^writeLEU/writeTPC/$',views.writeTPC,name="writeLEU/writeTPC"),
    url(r'^writeLEU/writeTSE/$',views.writeTSE,name="writeLEU/writeTSE"),


    url(r'^about/$',views.about,name="about"),
    url(r'^readLEU/$',views.readLEU,name="readLEU"),

    url(r'^analysizeTelegram/$',views.analysizeTelegram,name="analysizeTelegram"),
    url(r'^analysizeTelegram/analysizeTele/$',views.analysizeTele,name="analysizeTelegram/analysizeTele"),
    url(r'^analysizeTelegram/extractTele/$',views.extractTele,name="analysizeTelegram/extractTele"),

    url(r'^generateTelegram/$',views.generateTelegram,name="generateTelegram"),
    url(r'^testBaliseSwitch/$',views.testBaliseSwitch,name="testBaliseSwitch"),
    url(r'^testBaliseNoSwitch/$',views.testBaliseNoSwitch,name="testBaliseNoSwitch"),
    url(r'^test/$',views.test,name="test"),
    url(r'^admin/', admin.site.urls),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
