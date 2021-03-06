"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from rest_framework import routers
from adaapp import views
from django.contrib import admin
 
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'posts', views.PostViewSet)
router.register(r'factions', views.FactionViewSet)
router.register(r'agents', views.AgentViewSet)
 
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^create_agent/', views.create_agent, name='create_agent'),
    url(r'^get_agent/', views.get_agent, name='get_agent'),
    url(r'^verify_agent/', views.verify_agent, name='verify_agent'),
    url(r'^update_agent_ver_lvl/', views.update_agent_ver_lvl, name='update_agent_ver_lvl'),
    url(r'^get_agent_bynick/', views.get_agent_bynick, name='get_agent_bynick'),
    url(r'^update_agent_city/', views.update_agent_city, name='update_agent_city'),
    url(r'^update_trivia_points/', views.update_trivia_points, name='update_trivia_points'),
    url(r'^update_profile_picture/', views.update_profile_picture, name='update_profile_picture'),
    url(r'^topten_list/', views.topten_list, name='topten_list'),
    url(r'^update_profile/', views.update_profile, name='update_profile')
    
]