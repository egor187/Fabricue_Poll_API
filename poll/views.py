from rest_framework import generics, permissions
from .models import Poll, Question, Answer
from .serializers import PollSerializer, QuestionSerializer, AnswerSerializer, SelfPollSerializer

from .permissions import IsAnswerOwnerOrReadOnly

class PollListAPIView(generics.ListAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [permissions.IsAdminUser]


class PollCreateAPIView(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [permissions.IsAuthenticated]


class PollDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class SelfPollListAPIView(generics.ListAPIView):
    queryset = Poll.objects.all()
    serializer_class = SelfPollSerializer

    def get_queryset(self):
        return Poll.objects.filter(user__id=self.kwargs.get("user_id"))


class QuestionListAPIView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionCreateAPIView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerListAPIView(generics.ListAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [permissions.IsAdminUser]


class SelfAnswerListAPIView(generics.ListAPIView):
    serializer_class = AnswerSerializer

    def get_queryset(self):
        return Answer.objects.filter(user__id=self.kwargs.get("user_id"))


class AnswerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAnswerOwnerOrReadOnly]


class AnswerCreateAPIView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

        related_questions_ids = Question.objects.filter(
            pk=serializer.data.get("question")).values_list("id", flat=True
                                                            )
        polls = Poll.objects.filter(questions__id__in=related_questions_ids)
        for poll in polls:
            poll.user.add(self.request.user)
            poll.save()
