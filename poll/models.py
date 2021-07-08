import datetime as dt

from django.db import models
from users.models import CustomUser


class Poll(models.Model):
    """
    Poll model
    """
    name = models.CharField(max_length=100, verbose_name="name of the poll")
    started_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField()
    description = models.TextField()
    user = models.ManyToManyField(CustomUser, related_name="users", editable=False)

    def __str__(self):
        return self.name

    @property
    def is_active(self):
        return dt.datetime.today() < self.expired_at


class Question(models.Model):
    """
    Question model
    """
    CHOICES = [
        ("text", "text answer"),
        ("choice", "choice answer"),
        ("multiple", "multiple choice answer"),
    ]

    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="questions")
    text = models.TextField(verbose_name="text of a question")
    type = models.TextField(verbose_name="type of a question", choices=CHOICES)

    def __str__(self):
        return f"Question: {self.text}"


class Answer(models.Model):
    """
    Answer model
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="answers")
    text = models.TextField(verbose_name="Text of the answer")

    def __str__(self):
        return f"Answer {self.text} for question {self.question}"
