from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class MovieListAV(APIView):
    def get(self,request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class MovieDetailAV(APIView):
    def get(self,request,pk):
        try:
            movies = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'Error':'Movie Not Found'},status=status.HTTP_404_NOT_FOUND)    
        serializer = MovieSerializer(movies)
        return Response(serializer.data)

    def put(self,request,pk):
        movies = Movie.objects.get(pk=pk)   
        serializer = MovieSerializer(movies,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self,request,pk):
        movies = Movie.objects.get(pk=pk)
        movies.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        