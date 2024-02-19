from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Feed # models 에 가면 Feed 있음
from .serializers import FeedSerializer

class Feeds(APIView):
    
    def get(self, request):
        feeds = Feed.objects.all()

        # 객체 -> JSON (시리얼 라이즈)
        serializer = FeedSerializer(feeds, many=True)

        return Response(serializer.data)

    def post(self,request):
        # 역직렬화 (클라이언트가 보내준 json -> object)
        serializer = FeedSerializer(data=request.data)  
        # You must call `.s_valid()` before calling `.save() 
        # 세이브를 사용하려면 is_vaild 를 사용해야함
        if serializer.is_valid():
            feed = serializer.save(user=request.user)
            serializer = FeedSerializer(feed)    

            return Response(serializer.data) 
        else:
            return Response(serializer.errors)
    


class FeedDetail(APIView):
    def get_object(self, feed_id):
        # feed = Feed.objects.get(id=feed_id)
        try:
            return Feed.objects.get(id=feed_id)
        except Feed.DoesNotExist:
            raise NotFound
        
    def get(self,request, feed_id):
        feed = self.get_object(feed_id)

        serializer = FeedSerializer(feed)

        return Response(serializer.data)
