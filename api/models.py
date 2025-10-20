from django.db import models

class Biography(models.Model):
    year = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    media_url = models.FileField(upload_to='biography_media/', blank=True, null=True)

    def __str__(self):
        return f"{self.year} - {self.title}"

class Achievement(models.Model):
    CATEGORY_CHOICES = [
        ('education', 'Education'),
        ('economy', 'Economy'),
        ('infrastructure', 'Infrastructure'),
        ('social', 'Social'),
        ('foreign_policy', 'Foreign Policy'),
    ]
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField()
    image_url = models.ImageField(upload_to='achievements/')

    def __str__(self):
        return self.title

class Speech(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    transcript = models.TextField()
    audio_url = models.FileField(upload_to='speeches/')

    def __str__(self):
        return self.title

class GalleryItem(models.Model):
    title = models.CharField(max_length=255)
    image_url = models.ImageField(upload_to='gallery/')
    category = models.CharField(max_length=100)
    year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title

class QuizQuestion(models.Model):
    question = models.CharField(max_length=500)
    options = models.JSONField()  # Store options as a list of strings
    correct_answer = models.CharField(max_length=255)

    def __str__(self):
        return self.question

class CommunityPost(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    photo = models.ImageField(upload_to='community_posts/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post by {self.name} at {self.created_at.strftime('%Y-%m-%d %H:%M')}"
