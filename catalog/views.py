from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets, status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Catalog
from .serializers import CatalogSerialiser


class CatalogViewSet(ListCreateAPIView):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerialiser


class CatalogResp(APIView):

    #@csrf_exempt
    def get(self, request):


        return Response({'is_success': False, 'message': 'Please enter the valid date of birth.'})
