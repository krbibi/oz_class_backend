# 유저의 정보를 더 다양하게 보기 위해 depth = 1 작성 
# 다만 너무 많은 개인정보를 노출하고 있으니 필터를 거쳐 수정하기 위함

from rest_framework.serializers import ModelSerializer
from .models import User

class MyInfoUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class FeedUserSerializer(ModelSerializer):
    class Meta:
        model = User
        #fields = "__all__"
        fields = ("username","email","is_superuser",)