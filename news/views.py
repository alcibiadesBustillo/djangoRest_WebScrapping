from django.shortcuts import render
from django.http import JsonResponse

#----------------------------------------------
from rest_framework.decorators import api_view
from rest_framework.response import Response
#----------------------------------------------

from .serializers import NewsSerializers
from .models import News

# Create your views here.
@api_view(['GET'])
def newsOverview(request):
    api_urls = {
        'List': '/news-list/',
        'Detail View': '/news-detail/<str:pk>/',
        'Create': '/news-create/',
        'Update': '/news-update/<str:pk>/',
        'Delete': '/news-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def newsList(resquest):
    news = News.objects.all()
    serializer = NewsSerializers(news, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def newsDetail(resquest, pk):
    news = News.objects.get(id=pk)
    serializer = NewsSerializers(news, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def newsCreate(resquest):
    serializer = NewsSerializers(data=resquest.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def newsUpdate(resquest, pk):
    news = News.objects.get(id=pk)
    serializer = NewsSerializers(instance=news, data=resquest.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def newsDelete(resquest, pk):
    news = News.objects.get(id=pk)
    news.delete()
    return Response("Item succsesfully delete!")

