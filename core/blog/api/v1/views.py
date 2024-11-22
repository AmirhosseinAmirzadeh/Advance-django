from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import PostSerializer
from ...models import Post

@api_view()
def postList(request):
    return Response("Hello AmirHossein")


@api_view()
def postDetail(request, id):
    post = Post.objects.get(pk=id, status=True)
    serializer = PostSerializer(post)
    print(serializer.data)
    return Response(serializer.data)