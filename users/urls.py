from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'institute', InstituteViewSet)
router.register(r'profileRole', ProfileRoleViewSet)
router.register(r'profile', ProfileViewSet)
router.register(r'group', GroupViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('changePassword/', ChangePasswordView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('login/', LoginView.as_view()),
]