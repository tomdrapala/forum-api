from django.views.generic import ListView

from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'blog/list.html'

    def get_queryset(self):
        return Post.objects.all()
