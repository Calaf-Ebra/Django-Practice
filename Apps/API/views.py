from django.shortcuts import render
from django.http import JsonResponse
from .models import DATA
from .serializers import DataSer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def drink_list(request):
    if request.method == 'GET':
        drinks =DATA.objects.all()
        sers =DataSer(drinks, many=True)
        return JsonResponse({'drinks':sers.data})
    
    if request.method == 'POST':
        sers=DataSer(data = request.data)
        if sers.is_valid():
            sers.save()
            return Response(sers.data,status= status.HTTP_201_CREATED)
        
@api_view(['GET','PUT','DELETE'])
def drink_detail(request,id):

    try:
       drink = DATA.objects.get(pk=id)
    except DATA.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        sers = DataSer(drink)
        return Response(sers.data)
    
    elif request.method == 'PUT':
        sers =DataSer(drink,data=request.data)
        if sers.is_valid():
            sers.save()
            return Response(sers.data)
        return Response(sers.errors,status= status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




