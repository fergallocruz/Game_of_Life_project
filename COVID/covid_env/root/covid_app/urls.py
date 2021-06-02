from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'state_s', views.StateSexSet, basename="state_s")
router.register(r'state_a', views.StateSexAgeSet, basename="state_a")

urlpatterns = [
    path('', views.index, name='index'),
    path('radial/', views.radial, name='radial'),
    path('bubble/', views.bubble, name='bubble'),
    path('multiple/', views.multiple, name='multiple bars'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
