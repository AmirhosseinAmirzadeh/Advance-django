from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .serializer import PostSerializer
from ...models import Post
from django.shortcuts import get_object_or_404
from rest_framework import status, mixins
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListAPIView


@api_view(["GET", "POST"])
def postList(request):
    if request.method == "GET":
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(request.data)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticatedOrReadOnly])
def postDetail(request, id):
    post = get_object_or_404(Post, pk=id, status=True)
    if request.method == "GET":
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        post.delete()
        return Response({"detail":"✅ Item removed successfully"}, status=status.HTTP_204_NO_CONTENT)


# class PostList(APIView):
#     """getting a list of posts and creating new posts"""
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer
    
#     def get(self, request):
#         """retrieving a list of posts"""
#         posts = Post.objects.filter(status=True)
#         serializer = self.serializer_class(posts, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         """creating a post with provided data"""
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    
class PostDetail(APIView):
    """ getting detail of the post and edit plus removing it """

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get(self,request,id):
        """ retrieving post detail """
        post = get_object_or_404(Post, pk=id, status=True)
        serializer = self.serializer_class(post)
        return Response(serializer.data)
    
    def put(self,request,id):
        """ edit post detail """
        post = get_object_or_404(Post, pk=id, status=True)
        serializer = self.serializer_class(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self,request,id):
        """ delete post detail """
        post = get_object_or_404(Post, pk=id, status=True)
        post.delete()
        return Response({"detail":"✅ Item removed successfully"}, status=status.HTTP_204_NO_CONTENT)


# class PostList(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
#     """getting a list of posts and creating new posts"""
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer
#     queryset = Post.objects.filter(status=True)
    
#     def get(self, request, *args, **kwargs):
#         """ retrieving a list of posts """
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         """ create post """
#         return self.create(request, *args, **kwargs)


class PostList(ListAPIView):
    """getting a list of posts and creating new posts"""
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)