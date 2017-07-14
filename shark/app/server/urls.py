"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
import rest_framework
from rest_framework.routers import DefaultRouter
from nfl.views import TeamViewSet, GameViewSet, LeagueViewSet, UserViewSet

router = DefaultRouter()
router.register(prefix='teams', viewset=TeamViewSet)
router.register(prefix='games', viewset=GameViewSet)
router.register(prefix='users', viewset=UserViewSet)
router.register(prefix='leagues', viewset=LeagueViewSet)

urlpatterns = router.urls
urlpatterns += [
    url(r'^admin/', admin.site.urls),
]
