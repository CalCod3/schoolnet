from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from .serializers import ContactSerializer
from .forms import ContactForm

def landing_view(request, *args, **kwargs):
    
    template = 'landing.html'
    form = ContactForm
    
    return render(request, template, {'form': form})

@api_view(['POST'])
def contactAPI(request):
    serializer = ContactSerializer(data=request.data)
    is_ajax = request.META.get("CONTENT_TYPE") == "application/json"

    if serializer.is_valid() and request.is_ajax():
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    else:
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

