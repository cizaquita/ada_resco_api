import json
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from adaapp.models import *
from adaapp.serializers import *
 
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


#
#   API URLs
#
@csrf_exempt
def create_agent(request):
    """
    Crear Agente
    :param request
    :return json(succes or error):
    """
    if request.method == "POST":

        name = request.POST.get("name")
        telegram_nick = request.POST.get("telegram_nick")
        telegram_id = request.POST.get("telegram_id")
        try:
            Agent.objects.get(telegram_id=telegram_id)
            return JsonResponse({'status':'error', 'response':'Agente ya está creado'})
        except:
            agent = Agent(name=name, telegram_nick=telegram_nick, telegram_id=telegram_id)
            agent.save()
            return JsonResponse({'agente':agent.id, 'nombre':agent.name, 'tg nick':agent.telegram_nick, 'tg ID':agent.telegram_id})
    else:
        return JsonResponse({'status':'error', 'response':'request invalido'})

@csrf_exempt
def get_agent(request):
    if request.method == "POST":
        telegram_id = request.POST.get("telegram_id")

        try:
            agent = Agent.objects.get(telegram_id=telegram_id)
            return JsonResponse({"name":agent.name,"city":agent.city,"verified":agent.verified,"ingress_nick":agent.ingress_nick,"ingress_level":agent.ingress_level,"telegram_nick":agent.telegram_nick,"telegram_id":agent.telegram_id, "trivia_points":agent.trivia_points})
        except:
            return JsonResponse({'status':'error', 'response':'usuario no encontrado'})
    else:
        return JsonResponse({'status':'error', 'response':'request invalido'})