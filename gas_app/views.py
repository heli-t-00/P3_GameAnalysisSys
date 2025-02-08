from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Game, Point, Shot
from .serializers import GameSerializer, PointSerializer, ShotSerializer, GameNameSerializer


class GameListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the game items for given requested user
        '''
        Games = Game.objects.filter(user = request.user.id)
        serializer = GameSerializer(Games, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Game with given Game data
        '''
        # TODO fix this and update-------------
        data = {
            'task': request.data.get('task'),
            'completed': request.data.get('completed'),
            'user': request.user.id
        }
        serializer = GameSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GameDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, game_id, user_id):
        '''
        Helper method to get the object with given game_id, and user_id
        '''
        try:
            return Game.objects.get(id=game_id, user = user_id)
        except Game.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, game_id, *args, **kwargs):
        '''
        Retrieves the Game with given game_id
        '''
        game_instance = self.get_object(game_id, request.user.id)
        if not game_instance:
            return Response(
                {"res": "Object with game id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = GameSerializer(game_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, game_id, *args, **kwargs):
        '''
        Updates the game item with given _id if exists
        '''
        game_instance = self.get_object(game_id, request.user.id)
        if not game_instance:
            return Response(
                {"res": "Object with game id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'task': request.data.get('task'),
            'completed': request.data.get('completed'),
            'user': request.user.id
        }
        serializer = GameSerializer(instance = game_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, game_id, *args, **kwargs):
        '''
        Deletes the game item with given game_id if exists
        '''
        game_instance = self.get_object(game_id, request.user.id)
        if not game_instance:
            return Response(
                {"res": "Object with game id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        game_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )