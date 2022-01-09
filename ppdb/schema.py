import graphene
from graphene_django import DjangoObjectType

from polls.models import Choice, Question


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ("id", "pub_date", "question_text")


class ChoiceType(DjangoObjectType):
    class Meta:
        model = Choice
        fields = ("id", "question", "choice_text", "votes")


class Query(graphene.ObjectType):
    all_question = graphene.List(QuestionType)

    def resolve_all_question(root, info):
        # We can easily optimize query count in the resolve method
        return Question.objects.all()


schema = graphene.Schema(query=Query)
