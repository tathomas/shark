from rest_framework import viewsets
from nfl.models import Team, Game
from nfl.serializers import TeamSerializer, GameSerializer

class TeamViewSet(viewsets.ModelViewSet):
	""" ViewSet for viewing and editing Team objects """
	queryset = Team.objects.all()
	serializer_class = TeamSerializer

class GameViewSet(viewsets.ModelViewSet):
	""" ViewSet for viewing and editing Game objects """
	queryset = Game.objects.all()
	serializer_class = GameSerializer

