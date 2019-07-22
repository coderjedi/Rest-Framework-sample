

# Create your views here.
from rest_framework import generics

from .models import Post
from .serializers import PostSerializer


# class PostList(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

from . models import Post
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly


class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    """
    List all Posts, or create a new Post.
    """
    # def get(self, request, format=None):
    #     Posts = Post.objects.all()
    #     serializer = PostSerializer(Posts, many=True)
    #     return Response(serializer.data)
    #
    # def post(self, request, format=None):
    #     serializer = PostSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def delete(self, request, pk, format=None):
    #     Post = self.get_object(pk)
    #     Post.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Post.objects.all()                           # TO give access token use postman,add header as Authentication and value as Bearer access token
    serializer_class = PostSerializer
    """
    Retrieve, update or delete a Post instance.
    """

    # def get_object(self, pk):
    #     try:
    #         return Post.objects.get(id=pk)
    #     except Post.DoesNotExist:
    #         raise Http404

    # def get(self, request, pk, format=None):
    #     Post = self.get_object(pk)
    #     Post = PostSerializer(Post)
    #     return Response(Post.data)
    #
    # def put(self, request, pk, format=None):
    #     Post = self.get_object(pk)
    #     serializer = PostSerializer(Post, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def delete(self, request, pk, format=None):
    #     Post = self.get_object(pk)
    #     Post.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
