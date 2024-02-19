from django.shortcuts import render
from .models import Review
from .serializers import ReviewSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
# api/v1/reviews [GET]

class Reviews(APIView):
    def get(self,request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews,many=True) # reviews 여러개가 담겨있어 many=True 써줘야함
        
        return Response(serializer.data)

# api/v1/reviews/review_id [GET]
    
class ReviewDetail(APIView):
    def get(self, request, review_id):
        try:
            review = Review.objects.get(id=review_id)
        except:
            raise NotFound
        
        serializer = ReviewSerializer(review)

        return Response(serializer.data)