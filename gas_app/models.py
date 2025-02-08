from django.db import models

# Create your models here.

from django.contrib.auth.models import User


class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Point(models.Model):
    game_id = models.ForeignKey("Game", on_delete=models.CASCADE, to_field='id', related_name='points')
    total = models.IntegerField()
    team_a = models.IntegerField()

    def __str__(self):
        return f"T{self.total} A{self.team_a}"


class Shot(models.Model):
    point_id = models.ForeignKey("Point", on_delete=models.CASCADE, to_field='id', related_name='shots')
    a1x = models.FloatField()
    a1y = models.FloatField()
    b1x = models.FloatField()
    b1y = models.FloatField()
    sx = models.FloatField()
    sy = models.FloatField()

    def __str__(self):
        return f"A{self.a1x},{self.a1y} B{self.b1x},{self.b1y} S{self.sx},{self.sy}"
