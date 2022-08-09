from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Lobby

# Create your views here.

@api_view(['GET'])
def getData(request):
    lobby = Lobby.objects.all()
    return Response(lobby)