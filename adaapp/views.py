# -*- coding: utf-8 -*-

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
    # permission_classes = (IsAuthenticated,)
 
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
    # permission_classes = (IsAdminUser,)

class FactionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Faction.objects.all()
    serializer_class = FactionSerializer
    # permission_classes = (IsAdminUser,)

class AgentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    # permission_classes = (IsAdminUser,)


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

        telegram_nick = request.POST.get("telegram_nick")
        telegram_id = request.POST.get("telegram_id")

        try:
            Agent.objects.get(telegram_id=telegram_id)
            return JsonResponse({'status':'error', 'response':'Agente ya está creado'})
        except:
            agent = Agent(telegram_nick=telegram_nick, telegram_id=telegram_id)
            agent.save()
            return JsonResponse({
                'status':'ok',
                'id': agent.id,
                "name": agent.telegram_nick,
                'telegram_nick': agent.telegram_nick,
                'telegram_id': agent.telegram_id
            })
    else:
        return JsonResponse({'status':'error', 'response':'request invalido'})

@csrf_exempt
def get_agent(request):
    if request.method == "POST":
        telegram_id = request.POST.get("telegram_id")

        try:
            agent = Agent.objects.get(telegram_id=telegram_id)
            return JsonResponse({
                'status':'ok',
                "name": agent.telegram_nick,
                "city":agent.city,
                "verified":agent.verified,
                "ingress_nick":agent.ingress_nick,
                "ingress_level":agent.ingress_level,
                "telegram_nick":agent.telegram_nick,
                "telegram_id":agent.telegram_id,
                "trivia_points":agent.trivia_points,
                "verified_for":agent.verified_for,
                "verified_level":agent.verified_level,
                "profile_picture":agent.profile_picture
            })
        except:
            return JsonResponse({'status':'error', 'response':'usuario no encontrado'})
    else:
        return JsonResponse({'status':'error', 'response':'request invalido'})


@csrf_exempt
def get_agent_bynick(request):
    if request.method == "POST":
        telegram_nick = request.POST.get("telegram_nick")
        #agent = Agent.objects.get(telegram_nick=telegram_nick)

        try:
            agent = Agent.objects.get(telegram_nick__iexact=telegram_nick)
            return JsonResponse({
                'status':'ok',
                "name": agent.telegram_nick,
                "city":agent.city,
                "verified":agent.verified,
                "ingress_nick":agent.ingress_nick,
                "ingress_level":agent.ingress_level,
                "telegram_nick":agent.telegram_nick,
                "telegram_id":agent.telegram_id,
                "trivia_points":agent.trivia_points,
                "verified_for":agent.verified_for,
                "verified_level":agent.verified_level,
                "profile_picture":agent.profile_picture
            })
        except:
            return JsonResponse({'status':'error', 'response':'usuario no encontrado'})
    else:
        return JsonResponse({'status':'error', 'response':'request invalido'})

@csrf_exempt
def verify_agent(request):
    if request.method == "POST":
        telegram_id = request.POST.get("telegram_id")
        verified_for = request.POST.get("verified_for")

        try:
            agent = Agent.objects.get(telegram_id=telegram_id)
            agent.verified = True
            agent.verified_for = verified_for
            agent.save()
            return JsonResponse({'status':'ok',"name":agent.name,"verified":agent.verified})
        except:
            return JsonResponse({'status':'error', 'response':'usuario no encontradox'})
    else:
        return JsonResponse({'status':'error', 'response':'request invalido'})

@csrf_exempt
def update_agent_ver_lvl(request):
    if request.method == "POST":
        telegram_id = request.POST.get("telegram_id")
        verified_level = request.POST.get("verified_level")
        verified_for = request.POST.get("verified_for")

        try:
            agent = Agent.objects.get(telegram_id=telegram_id)
            agent.verified_level = verified_level
            agent.verified_for = verified_for
            agent.verified = True
            agent.save()
            return JsonResponse({
                'status':'ok',
                "telegram_nick":agent.telegram_nick,
                'name':agent.name,
                "verified_level":agent.verified_level
            })
        except:
            return JsonResponse({'status':'error', 'response':'usuario no encontrado'})
    else:
        return JsonResponse({'status':'error', 'response':'request invalido'})
    
@csrf_exempt
def update_agent_city(request):
    if request.method == "POST":
        telegram_id = request.POST.get("telegram_id")
        agent_city = request.POST.get("agent_city")

        try:
            agent = Agent.objects.get(telegram_id=telegram_id)
            agent.city = agent_city
            agent.save()
            return JsonResponse({
                'status':'ok',
                "name":agent.telegram_nick,
                "verified_level":agent.verified_level
            })
        except:
            return JsonResponse({'status':'error', 'response':'usuario no encontrado'})
    else:
        return JsonResponse({'status':'error', 'response':'request invalido'})

@csrf_exempt
def update_trivia_points(request):
    if request.method == "POST":
        telegram_id = request.POST.get("telegram_id")
        action = request.POST.get("action")
        points = request.POST.get("points")
        try:
            agent = Agent.objects.get(telegram_id=telegram_id)
            if action == "sumar":
                agent.trivia_points += int(points)
            else:
                agent.trivia_points -= int(points)
            agent.save()
            return JsonResponse({
                'status':'ok',
                "name":agent.telegram_nick,
                "trivia_points":agent.trivia_points
            })
        except Exception as e:
            return JsonResponse({'status':'error', 'response':'usuario no encontrado o ' + str(e)})
    else:
        return JsonResponse({'status':'error', 'response':'request invalido'})

@csrf_exempt
def update_profile_picture(request):
    if request.method == "POST":
        telegram_id = request.POST.get("telegram_id")
        profile_picture = request.POST.get("profile_picture")
        try:
            agent = Agent.objects.get(telegram_id=telegram_id)
            agent.profile_picture = profile_picture
            agent.save()
            return JsonResponse({
                'status':'ok',
                "telegram_nick":agent.telegram_nick,
                "profile_picture":agent.profile_picture
            })
        except:
            return JsonResponse({'status':'error', 'response':'usuario no encontrado'})
    else:
        return JsonResponse({'status':'error', 'response':'request invalido'})


@csrf_exempt
def topten_list(request):
    """
    Lista de agentes TOP TEN TRIIA
    :return json(agentes):
    """
    if request.method == "POST":

        result = Agent.objects\
            .values('ingress_nick','telegram_nick','trivia_points')
        result = list(result)

        return HttpResponse(json.dumps(result, cls=DjangoJSONEncoder))
    else:
        return JsonResponse({'status':'error', 'response':'request invalido'})