from watchlist_app.models import *
from watchlist_app.api.serializers import WatchListSerializer, StreamPlatFromSerializer,ReviewSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from rest_framework.views import APIView
from rest_framework import generics,mixins
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError

class ReviewList(generics.ListAPIView):
    # queryset = Review.objects.all()

    serializer_class = ReviewSerializer
    
    
    
    
    def get_queryset(self):
        watchlist_pk = self.kwargs.get('pk')
        return Review.objects.filter(watchlist_id=watchlist_pk)

class ReviewCreateView(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        return Review.objects.all()
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        watchlist = WatchList.objects.get(pk=pk)
        review_user = self.request.user
        review_queryset = Review.objects.filter(watchlist=watchlist,review_user=review_user)
        if review_queryset.exists():
            raise ValidationError('You have already reviewed this movie')
        serializer.save(watchlist_id=self.kwargs.get('pk'),review_user=review_user)

class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
    
#     def get(self,request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class ReviewDetailView(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
    
#     def get(self,request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

class WatchListView(APIView):
    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)

class MovieDetailView(APIView):
    def get(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie)
        return Response(serializer.data)
    def put(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    def delete(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class StreamPlatFormViewSet(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatFromSerializer


# class StreamPlatFormViewSet(viewsets.ViewSet):
#     def list(self,request):
#         stream_platforms = StreamPlatform.objects.all()
#         serializer = StreamPlatFromSerializer(stream_platforms, many=True)
#         return Response(serializer.data)
    
#     def retrive(self,request,pk=None):
#         stream_platform = StreamPlatform.objects.get(pk=pk)
#         serializer = StreamPlatFromSerializer(stream_platform)
#         return Response(serializer.data)
    
# class StreamPlatFormListView(APIView):
#     def get(self, request):
#         stream_platforms = StreamPlatform.objects.all()
#         serializer = StreamPlatFromSerializer(stream_platforms, many=True)
#         return Response(serializer.data)
#     def post(self, request):
#         serializer = StreamPlatFromSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors)
        
# class StreamPlatFormDetailView(APIView):
#     def get(self, request, pk):
#         stream_platform = StreamPlatform.objects.get(pk=pk)
#         serializer = StreamPlatFromSerializer(stream_platform)
#         return Response(serializer.data)
#     def post(self, request, pk):
#         stream_platform = StreamPlatform.objects.get(pk=pk)
#         serializer = StreamPlatFromSerializer(stream_platform, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#     def delete(self, request, pk):
#         stream_platform = StreamPlatform.objects.get(pk=pk)
#         stream_platform.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    

# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies,many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
        
# @api_view(['GET', 'POST','DELETE'])
# def movie_detail(request,pk):
#     if request.method == 'GET':
#         movies = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movies)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
        
#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)