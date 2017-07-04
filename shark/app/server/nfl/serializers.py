from rest_framework import serializers
from nfl.models import Team, Game, League, User

class TeamSerializer(serializers.ModelSerializer):
	""" Serializer to represent Team model """
	class Meta:
		model = Team
		fields = ("location", "name", "wins", "losses", "ties")

class GameSerializer(serializers.ModelSerializer):
	""" Serializer to represent Game model """
	class Meta:
		model = Game
		fields = ("team_1", "team_2", "score_1", "score_2", "date")

class LeagueSerializer(serializers.ModelSerializer):
	""" Serializer to represent League model """
	class Meta:
		model = League
		fields = ("members", "name")

class UserSerializer(serializers.ModelSerializer):
	""" Serializer to represent User model """
	class Meta:
		model = User
		fields = ("username", "password", "email_address", "first_name", "last_name")

