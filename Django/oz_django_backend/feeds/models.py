from django.db import models
from common.models import CommonModel
# 제목 내용 작성자 
# Feed 와 User의 관계
# User -> Feed, Feed, Feed  가능 (유저가 여러개 게시글 작성 가능)
# Feed -> User, User, User (하나의 게시글 여러개 유저 ? 불가능)
# User:Feed = 1:N => User(1):Feed(N)


class Feed(CommonModel):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=120)

    user = models.ForeignKey("users.User",on_delete=models.CASCADE)
