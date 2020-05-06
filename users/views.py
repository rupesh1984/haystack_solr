from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from .models import UserModel
from .serialzers import UserSerializer
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser



class UserView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    @api_view(['GET'])
    def list_users(request):
        users = UserModel.objects.all().order_by('-date_created')
        list_of_users = UserSerializer(users, many=True)
        return JsonResponse(list_of_users.data, safe=False)

    @api_view(['POST'])
    def create_user(request):
        print("Methos is ", request.method)

        #print("Methos is ", request.method)
        #user_data = JSONParser.parse(request.data)
        user_data_serliase = UserSerializer(data=request.data)
        if user_data_serliase.is_valid():
            user_data_serliase.save()

            return JsonResponse(user_data_serliase.data, status= status.HTTP_201_CREATED)
        else:
            return JsonResponse({"data": "Fail to save data"}, status=status.HTTP_400_BAD_REQUEST)



