from rest_framework import serializers
from .models import Game, Point, Shot


class ShotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shot
        fields = '__all__'


class PointSerializer(serializers.ModelSerializer):
    shots = ShotSerializer(many=True, required=False)

    class Meta:
        model = Point
        fields = '__all__'


class GameSerializer(serializers.ModelSerializer):
    points = PointSerializer(many=True, required=False)

    class Meta:
        model = Game
        fields = '__all__'


class GameNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'
