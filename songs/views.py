from rest_framework import status 
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework.exceptions import NotFound 
from .models import * 
from .serializers.common import * 

class SongListCreate(APIView):

    def get(self, request):

        songs = Song.objects.all()

        serialized_songs = PopulatedSongSerializer(songs, many=True)

        return Response(data=serialized_songs.data, status=status.HTTP_200_OK)

    def post(self, request):

        song_serializer = SongSerializer(data=request.data)

        if song_serializer.is_valid():

            song_serializer.save()

            return Response(data=song_serializer.data, status=status.HTTP_200_OK)

        return Response(data=song_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SongRetrieveUpdateDelete(APIView):

    def get(self, request, pk):
        song = self.get_song(pk=pk)

        serialized_song = PopulatedSongSerializer(song)

        return Response(data=serialized_song.data, status=status.HTTP_200_OK)


    def put(self, request, pk):

        song_to_update = self.get_song(pk=pk)

        updated_song = SongSerializer(song_to_update, data=request.data)

        if updated_song.is_valid():

            updated_song.save()

            return Response(updated_song.data, status=status.HTTP_200_OK)

        return Response(data=updated_song.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):

        song_to_delete = self.get_song(pk=pk)
        song_to_delete.delete()       
        return Response(status=status.HTTP_204_NO_CONTENT)


    def get_song(self, pk):
        try:
            return Song.objects.get(pk=pk)
        except Song.DoesNotExist:
            raise NotFound(detail="Can't find that song")

class FilmListCreate(APIView):

    def get(self, request):

        films = Film.objects.all()

        serialized_films = FilmSerializer(films, many=True)

        return Response(data=serialized_films.data, status=status.HTTP_200_OK)

    def post(self, request):

        film_serializer = FilmSerializer(data=request.data)

        if film_serializer.is_valid():

            film_serializer.save()

            return Response(status=201)

        return Response(data=film_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FilmRetrieveUpdateDelete(APIView):

    def get(self, request, pk):
        film = self.get_film(pk=pk)

        serialized_film = PopulatedFilmSerializer(film)

        return Response(data=serialized_film.data, status=status.HTTP_200_OK)


    def put(self, request, pk):

        film_to_update = self.get_film(pk=pk)

        updated_film = FilmSerializer(film_to_update, data=request.data)

        if updated_film.is_valid():

            updated_film.save()

            return Response(updated_film.data, status=status.HTTP_200_OK)

        return Response(data=updated_film.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_film(self, pk):
        try:
            return Film.objects.get(pk=pk)
        except Film.DoesNotExist:
            raise NotFound(detail="Can't find that film")

class ArtistListCreate(APIView):
  def get(self, request):

        artists = Artist.objects.all()

        serialized_artists = PopulatedArtistSerializer(artists, many=True)

        return Response(data=serialized_artists.data, status=status.HTTP_200_OK)

  def post(self, request):

      name = request.data.get('name')
      try:
        existing_artist = Artist.objects.get(name=name)
        if existing_artist:
          return Response({'message': 'artist already exists'})
      except Artist.DoesNotExist:
          pass

      artist_serializer = ArtistSerializer(data=request.data)

      if artist_serializer.is_valid():

          artist_serializer.save()

          return Response(data=artist_serializer.data, status=status.HTTP_200_OK)

      return Response(data=artist_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArtistRetrieveUpdateDelete(APIView):

    def get(self, request, pk):
        artist = self.get_artist(pk=pk)

        serialized_artist = PopulatedArtistSerializer(artist)

        return Response(data=serialized_artist.data, status=status.HTTP_200_OK)


    def put(self, request, pk):

        artist_to_update = self.get_artist(pk=pk)

        updated_artist = ArtistSerializer(artist_to_update, data=request.data)

        if updated_artist.is_valid():

            updated_artist.save()

            return Response(updated_artist.data, status=status.HTTP_200_OK)

        return Response(data=updated_artist.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_artist(self, pk):
        try:
            return Artist.objects.get(pk=pk)
        except Artist.DoesNotExist:
            raise NotFound(detail="Can't find that artist")

class AlbumListCreate(APIView):
  def get(self, request):

        albums = Album.objects.all()

        serialized_albums = PopulatedAlbumSerializer(albums, many=True)

        return Response(data=serialized_albums.data, status=status.HTTP_200_OK)

  def post(self, request):

      name = request.data.get('name')
      try:
        existing_album = Album.objects.get(name=name)
        if existing_album:
          return Response({'message': 'album already exists'})
      except Album.DoesNotExist:
          pass

      album_serializer = AlbumSerializer(data=request.data)

      if album_serializer.is_valid():

          album_serializer.save()

          return Response(data=album_serializer.data, status=status.HTTP_200_OK)

      return Response(data=album_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AlbumRetrieveUpdateDelete(APIView):

    def get(self, request, pk):
        album = self.get_album(pk=pk)

        serialized_album = PopulatedAlbumSerializer(album)

        return Response(data=serialized_album.data, status=status.HTTP_200_OK)


    def put(self, request, pk):

        album_to_update = self.get_album(pk=pk)

        updated_album = AlbumSerializer(album_to_update, data=request.data)

        if updated_album.is_valid():

            updated_album.save()

            return Response(updated_album.data, status=status.HTTP_200_OK)

        return Response(data=updated_album.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_album(self, pk):
        try:
            return Album.objects.get(pk=pk)
        except Album.DoesNotExist:
            raise NotFound(detail="Can't find that album")

class ContextListCreate(APIView):
  def get(self, request):

        contexts = Context.objects.all()

        serialized_contexts = PopulatedContextSerializer(contexts, many=True)

        return Response(data=serialized_contexts.data, status=status.HTTP_200_OK)

  def post(self, request):

      song = request.data.get('song')
      film = request.data.get('film')
      try:
        existing_context = Context.objects.filter(song=song, film=film)
        if existing_context:
          print(existing_context)
          return Response({'message': 'context already exists'})
      except Context.DoesNotExist:
          pass

      context_serializer = ContextSerializer(data=request.data)

      if context_serializer.is_valid():

          context_serializer.save()

          return Response(data=context_serializer.data, status=status.HTTP_200_OK)

      return Response(data=context_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ContextUpdateDelete(APIView):

    def put(self, request, pk):

        context_to_update = self.get_context(pk=pk)

        updated_context = ContextSerializer(context_to_update, data=request.data)

        if updated_context.is_valid():

            updated_context.save()

            return Response(updated_context.data, status=status.HTTP_200_OK)

        return Response(data=updated_context.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_context(self, pk):
        try:
            return Context.objects.get(pk=pk)
        except Context.DoesNotExist:
            raise NotFound(detail="Can't find that context")

class ContextRetrieveBySongAndFilm(APIView):

    def get(self, request):

      songId = request.GET.get('songId')
      filmId = request.GET.get('filmId')
        
      context = list(Context.objects.filter(song=songId, film=filmId))

      serialized_context = PopulatedContextSerializer(context, many=True)

      return Response(data=serialized_context.data, status=status.HTTP_200_OK)

class ContextRetrieveAllForSong(APIView):

    def get(self, request):

      songId = request.GET.get('songId')
        
      context = list(Context.objects.filter(song=songId))

      serialized_context = PopulatedContextSerializer(context, many=True)

      return Response(data=serialized_context.data, status=status.HTTP_200_OK)

class ContextRetrieveAllForFilm(APIView):

    def get(self, request):

      filmId = request.GET.get('filmId')
        
      context = list(Context.objects.filter(film=filmId))

      serialized_context = PopulatedContextSerializer(context, many=True)

      return Response(data=serialized_context.data, status=status.HTTP_200_OK)