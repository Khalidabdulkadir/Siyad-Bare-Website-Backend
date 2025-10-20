from rest_framework import viewsets, permissions
from .models import (
    Biography, Achievement, Speech, GalleryItem, QuizQuestion, CommunityPost
)
from .serializers import (
    BiographySerializer, AchievementSerializer, SpeechSerializer, 
    GalleryItemSerializer, QuizQuestionSerializer, CommunityPostSerializer
)

class BiographyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows biography entries to be viewed.
    """
    queryset = Biography.objects.all().order_by('year')
    serializer_class = BiographySerializer
    permission_classes = [permissions.AllowAny]

class AchievementViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows achievements to be viewed.
    """
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    permission_classes = [permissions.AllowAny]

class SpeechViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows speeches to be viewed.
    """
    queryset = Speech.objects.all().order_by('year')
    serializer_class = SpeechSerializer
    permission_classes = [permissions.AllowAny]

class GalleryItemViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows gallery items to be viewed.
    """
    queryset = GalleryItem.objects.all()
    serializer_class = GalleryItemSerializer
    permission_classes = [permissions.AllowAny]

class QuizQuestionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows quiz questions to be viewed.
    """
    queryset = QuizQuestion.objects.all()
    serializer_class = QuizQuestionSerializer
    permission_classes = [permissions.AllowAny]

class CommunityPostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows community posts to be viewed or created.
    """
    queryset = CommunityPost.objects.all().order_by('-created_at')
    serializer_class = CommunityPostSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get', 'post', 'head', 'options']

