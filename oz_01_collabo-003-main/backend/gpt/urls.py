from django.urls import path
from . import views

urlpatterns = [
    path('quiz/<str:levelName>', views.GptQuizAPIView.as_view(), name="gpt_quiz_get"), # gpt 질문 답 피드백 가져오기
    path('feedback/<int:quiz_try_id>/',views.FeedbackView.as_view(), name="gpt_feedback"), # gpt 질문 답 피드백 저장
]