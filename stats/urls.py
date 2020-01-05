from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'CourseReview', CourseReviewsViewSet)
router.register(r'lessonReview', LessonReviewsViewSet)
router.register(r'enroll', CourseEnrollViewSet)
router.register(r'groupCourse', GroupCourseAllocationViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)