from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from adaapp.serializers import UserSerializer, GroupSerializer, PostSerializer, FactionSerializer, AgentSerializer
from adaapp.models import Post, Faction, Agent
 
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    #permission_classes = (IsAuthenticated,)
 
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    #permission_classes = (IsAdminUser,)

class FactionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Faction.objects.all()
    serializer_class = FactionSerializer
    #permission_classes = (IsAdminUser,)

class AgentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    #permission_classes = (IsAdminUser,)