from rest_framework import serializers
from nfl.models import Team, Game

class TeamSerializer(serializers.ModelSerializer):
	""" Serializer to represent Team model """
	class Meta:
		model = Team
		fields = ("location", "name", "wins", "losses", "ties")

class GameSerializer(serializers.ModelSerializer):
	""" Serializer to represent Game modes """
	class Meta:
		model = Game
		fields = ("team_1", "team_2", "score_1", "score_2", "date")
