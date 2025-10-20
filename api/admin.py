from django.contrib import admin
from .models import (
    Biography, Achievement, Speech, GalleryItem, QuizQuestion, CommunityPost
)

@admin.register(Biography)
class BiographyAdmin(admin.ModelAdmin):
    list_display = ('year', 'title')
    search_fields = ('title', 'description')

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    list_filter = ('category',)
    search_fields = ('title', 'description')

@admin.register(Speech)
class SpeechAdmin(admin.ModelAdmin):
    list_display = ('title', 'year')
    search_fields = ('title', 'transcript')

@admin.register(GalleryItem)
class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'year')
    list_filter = ('category',)
    search_fields = ('title',)

@admin.register(QuizQuestion)
class QuizQuestionAdmin(admin.ModelAdmin):
    list_display = ('question',)
    search_fields = ('question',)

@admin.register(CommunityPost)
class CommunityPostAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('created_at',)
