from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BiographyViewSet, AchievementViewSet, SpeechViewSet, 
    GalleryItemViewSet, QuizQuestionViewSet, CommunityPostViewSet
)

router = DefaultRouter()
router.register(r'biography', BiographyViewSet)
router.register(r'achievements', AchievementViewSet)
router.register(r'speeches', SpeechViewSet)
router.register(r'gallery', GalleryItemViewSet)
router.register(r'quiz', QuizQuestionViewSet)
router.register(r'community', CommunityPostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
