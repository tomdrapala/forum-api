from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, \
    get_object_or_404, CreateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated
from django.contrib.auth.models import User

from blog.models import Post
from .serializers import UserSerializer, UserCreateSerializer, PostSerializer, LikeSerializer
from .permissions import IsOwnerOrReadOnly


class UserList(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreateView(CreateAPIView):
    """
    This solution is not recommended to be used in a real project.
    It was created just to enable fast and easy User creation method, to facilitate application testing.
    """
    permission_classes = (AllowAny,)
    model = User
    serializer_class = UserCreateSerializer


class PostList(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class LikeView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def post(self, request, pk):
        post = get_object_or_404(Post, id=pk)
        serializer = LikeSerializer(post)
        serializer.update(post, self.request.user)
        return Response(status=HTTP_204_NO_CONTENT)
