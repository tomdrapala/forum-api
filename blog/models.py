from django.db import models


class Post(models.Model):
    author = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    liked_by = models.ManyToManyField('auth.User', related_name='liked_posts', blank=True)

    class Meta:
        ordering = ['-created_at']

    def like_count(self):
        return self.liked_by.count()

    def __str__(self):
        return f"{self.id} - {self.title}"
