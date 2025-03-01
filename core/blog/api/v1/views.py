from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .serializer import PostSerializer, CategorySerializer
from ...models import Post, Category
from django.shortcuts import get_object_or_404
from rest_framework import status, mixins
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets

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
    
# class PostDetail(APIView):
#     """ getting detail of the post and edit plus removing it """

#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer

#     def get(self,request,id):
#         """ retrieving post detail """
#         post = get_object_or_404(Post, pk=id, status=True)
#         serializer = self.serializer_class(post)
#         return Response(serializer.data)
    
#     def put(self,request,id):
#         """ edit post detail """
#         post = get_object_or_404(Post, pk=id, status=True)
#         serializer = self.serializer_class(post, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    
#     def delete(self,request,id):
#         """ delete post detail """
#         post = get_object_or_404(Post, pk=id, status=True)
#         post.delete()
#         return Response({"detail":"✅ Item removed successfully"}, status=status.HTTP_204_NO_CONTENT)


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


# class PostList(ListAPIView):
#     """getting a list of posts and creating new posts"""
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer
#     queryset = Post.objects.filter(status=True)


class PostList(ListCreateAPIView):
    """getting a list of posts and creating new posts"""
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    
# class PostDetail(GenericAPIView):
#     """ getting detail of the post and edit plus removing it """
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer
    
#     def get(self, request, id):
#         """ retrieving post detail """
#         post = get_object_or_404(Post, pk=id, status=True)
#         serializer = self.serializer_class(post)
#         return Response(serializer.data)


# class PostDetail(GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
#     """ getting detail of the post and edit plus removing it """
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer
#     queryset = Post.objects.filter(status=True)
    
#     def get(self, request, *args, **kwargs):
#         """ retrieving post detail """
#         return self.retrieve(request, *args, **kwargs)
    
#     def put(self, request, *args, **kwargs):
#         """ update post detail """
#         return self.update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         """ delete post detail """
#         return self.destroy(request, *args, **kwargs)
    

'''class PostDetail(RetrieveUpdateDestroyAPIView):
    """ getting detail of the post and edit plus removing it """
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)


class PostViewSet(viewsets.ViewSet):
    """ getting list and detail of the posts by using ViewSet """
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    def list(self, request):
        """ getting list of the posts """
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """ getting detail of the post """
        post = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(post)
        return Response(serializer.data)

    def create(self, request):
        """ create a new post """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def update(self, request, pk=None):
        """ update a post """
        post = get_object_or_404(Post, pk=pk)
        serializer = self.serializer_class(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
        
    def partial_update(self, request, pk=None):
        """ partial update a post """
        post = get_object_or_404(Post, pk=pk)
        serializer = self.serializer_class(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
        
    def destroy(self, request, pk=None):
        """ delete a post """
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)'''
    

class PostModelViewSet(viewsets.ModelViewSet):
    """ getting list and detail of the posts by using ViewSet """
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

class CategoryModelViewSet(viewsets.ModelViewSet):
    """ getting category of the posts """
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()