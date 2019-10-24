from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'Institute', InstituteViewSet)
router.register(r'ProfileRole', ProfileRoleViewSet)
router.register(r'Profile', ProfileViewSet)
router.register(r'Group', GroupViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('ChangePassword/', ChangePasswordView.as_view()),
    path('Logout/', LogoutView.as_view()),
    path('Login/', LoginView.as_view()),
]