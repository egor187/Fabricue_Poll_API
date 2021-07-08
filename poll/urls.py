from django.urls import path
from . import views


app_name = "poll"

urlpatterns = [
    path("polls/view/", views.PollListAPIView.as_view(), name="polls_index"),
    path("polls/create/", views.PollCreateAPIView.as_view(), name="polls_create"),
    path("polls/rud/<int:pk>/", views.PollDetailAPIView.as_view(), name="poll_detail"),
    path("polls/view/self/<int:user_id>", views.SelfPollListAPIView.as_view(), name="self_polls_index"),

    path("questions/view/", views.QuestionListAPIView.as_view(), name="questions_index"),
    path("questions/create/", views.QuestionCreateAPIView.as_view(), name="questions_index"),
    path("questions/rud/<int:pk>/", views.QuestionDetailAPIView.as_view(), name="question_detail"),

    path("answers/view/", views.AnswerListAPIView.as_view(), name="answer_index"),
    path("answers/create/", views.AnswerCreateAPIView.as_view(), name="answer_create"),
    path("answers/rud/<int:pk>/", views.AnswerDetailAPIView.as_view(), name="answer_index"),
    path("answers/view/self/<int:user_id>", views.SelfAnswerListAPIView.as_view(), name="self_answers_index"),

]
