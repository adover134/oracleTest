from rest_framework import routers
from django.urls import path
from testing import views

router = routers.SimpleRouter()
router.register('user', views.UserViewSets)
urlpatterns = [
    # path('some_functional_view_url', views.functional_view)
]
urlpatterns += router.urls