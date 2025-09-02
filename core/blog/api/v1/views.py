from django.shortcuts import get_object_or_404
from django.db.models import Count, Q

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import mixins
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from blog.models import Post, Category
from rest_framework.views import APIView

from .paginations import DefaultPagination
from .serializers import PostSerializer, CategorySerializer
from .permissions import IsOwnerOrReadOnly


class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {'category': ['exact', 'in'], 'author':['exact'], 'status': ['exact']}
    search_fields = ['title', 'content']
    ordering_fields = ['published_date', 'id']
    pagination_class = DefaultPagination

    @action(detail=False, methods=['get'])
    def get_summary(self, request):
        posts_count = Post.objects.aggregate(
            published_count=Count('id', filter=Q(status=True)),
            unpublished_count=Count('id', filter=Q(status=False))
        )
        return Response(posts_count)


class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


'''
class PostListApi(APIView):
    """getting a list of posts and creating new posts"""
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get(self, request):
        """retrieving a list of post"""
        posts = Post.objects.filter(status=True)
        serializer = self.serializer_class(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        """"creating a post with provided data"""
        serializer = self.serializer_class(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
'''


'''class PostListApi(GenericAPIView):
    """getting a list of posts and creating new posts"""
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    def get(self, request):
        """retrieving a list of post"""
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        """"creating a post with provided data"""
        serializer = self.serializer_class(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)'''


'''class PostListApi(mixins.ListModelMixin, mixins.CreateModelMixin,
                  GenericAPIView):
    """getting a list of posts and creating new posts"""
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    def get(self, request, *args, **kwargs):
        """retrieving a list of post"""
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """retrieving a list of post"""
        return self.create(request, *args, **kwargs)
'''

'''class PostListApi(ListCreateAPIView):
    """getting a list of posts and creating new posts"""
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)'''

'''
class PostDetailApi(APIView):
    """getting detail of the post and edit plus removing it"""
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get(self, request, pk):
        """retrieving the post data"""
        post = get_object_or_404(Post, pk=pk, status=True)
        serializer = self.serializer_class(post)
        return Response(serializer.data)

    def put(self, request, pk):
        """editing the post data"""
        post = get_object_or_404(Post, pk=pk, status=True)
        serializer = self.serializer_class(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        """deleting the post object"""
        post = get_object_or_404(Post, pk=pk, status=True)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''

'''class PostDetailApi(GenericAPIView):
    """getting detail of the post and edit plus removing it"""
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    def get(self, request, pk):
        """retrieving the post data"""
        post = self.get_object()
        serializer = self.serializer_class(post)
        return Response(serializer.data)

    def put(self, request, pk):
        """editing the post data"""
        post = self.get_object()
        serializer = self.serializer_class(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        """deleting the post object"""
        post = self.get_object()
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''

'''class PostDetailApi(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin, GenericAPIView):
    """getting detail of the post and edit plus removing it"""
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    def get(self, request, pk, *args, **kwargs):
        """retrieving the post data"""
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, pk, *args, **kwargs):
        """editing the post data"""
        return self.update(request, *args, **kwargs)

    def delete(self, request, pk, *args, **kwargs):
        """deleting the post object"""
        return self.destroy(request, *args, **kwargs)
'''

'''class PostDetailApi(RetrieveUpdateDestroyAPIView):
    """getting detail of the post and edit plus removing it"""
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)'''


'''class PostViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, pk, *args, **kwargs):
        post = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(post)
        return Response(serializer.data)

    def update(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        serializer = self.serializer_class(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        serializer = self.serializer_class(post, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk, *args, **kwargs):
        post = get_object_or_404(self.queryset, pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''
