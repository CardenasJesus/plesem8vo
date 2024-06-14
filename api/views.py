from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import GrantGoal
from .serializer import ListGrantGoalSerializer, DetailGrantGoalSerializer, CreateGrantGoalSerializer, UpdateGrantGoalSerializer

# Create your views here.

### API GrantGoal List ###

## RETRIVE

##create
class CreateGrantGoalAPIView(generics.CreateAPIView):
   serializer_class = CreateGrantGoalSerializer

## LIST
class GrantGoalListAPIView(APIView):
    def get(self, request):
        queryset = GrantGoal.objects.all()
        data = ListGrantGoalSerializer(queryset, many=True).data
        return Response(data)

### detail
class detailGrantGoalAPIView(APIView):
    def get(self, request, pk):
        queryset = GrantGoal.objects.get(pk=pk)
        data = DetailGrantGoalSerializer(queryset, many=False).data
        return Response(data)


### UPDATE

class UpdateGrantGoalAPIView(generics.UpdateAPIView):
    serializer_class = UpdateGrantGoalSerializer
    queryset = GrantGoal.objects.all()


### DELETE

class DeleteGrantGoalAPIView(generics.DestroyAPIView):
    serializer_class = DetailGrantGoalSerializer
    queryset = GrantGoal.objects.all()