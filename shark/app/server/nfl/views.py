from rest_framework import viewsets
from nfl.models import Team, Game, League, User
from nfl.serializers import TeamSerializer, GameSerializer, LeagueSerializer, UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
	""" ViewSet for viewing and editing Team objects """
	queryset = Team.objects.all()
	serializer_class = TeamSerializer

class GameViewSet(viewsets.ModelViewSet):
	""" ViewSet for viewing and editing Game objects """
	queryset = Game.objects.all()
	serializer_class = GameSerializer

class LeagueViewSet(viewsets.ModelViewSet):
	""" Viewset for viewing and editing League objects """
	queryset = League.objects.all()
	serializer_class = LeagueSerializer

class UserViewSet(viewsets.ModelViewSet):
	""" Viewset for viewing and editing User objects """
	queryset = User.objects.all()
	serializer_class = UserSerializer

