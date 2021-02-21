from django.contrib import admin
from django.urls import path, include
from characters.views import NPCViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'npc', NPCViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('characters/', include(router.urls)),
]
