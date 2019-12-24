from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'Assignment', AssignmentViewSet)
router.register(r'View', GradedAssignmentListView)
router.register(r'Create', GradedAssignmentCreateView)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
