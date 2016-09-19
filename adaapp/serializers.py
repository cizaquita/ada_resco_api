from django.contrib.auth.models import User, Group
from rest_framework import serializers
from adaapp.models import Post, Faction, Agent
 
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')
 
 
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'content', 'url')

class FactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Faction
        fields = ('name', 'image')

class AgentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Agent
        fields = ('name', 'faction', 'city', 'verified', 'profile_picture', 'ingress_nick', 'ingress_level', 'telegram_nick', 'telegram_id', 'geo_latitude', 'geo_longitude', 'verified_level', 'trivia_points', 'id')


