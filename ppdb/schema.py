import graphene
from graphene_django import DjangoObjectType
from hantamkoding import paginator
from polls.models import Choice, Question


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        filter_fields = {
            "pub_date": ["istartswith", "exact"],
            "question_text": ["icontains"]
        }


class ChoiceType(DjangoObjectType):
    class Meta:
        model = Choice
        fields = ("id", "question", "choice_text", "votes")


class Query(graphene.ObjectType):
    all_question = graphene.List(QuestionType)
    question_by_id = graphene.Field(
        QuestionType, id=graphene.String(required=True))

    questions = customers = paginator.DjangoPaginationConnectionField(
        QuestionType)

    def resolve_all_question(root, info):
        # We can easily optimize query count in the resolve method
        return Question.objects.all()

    def resolve_questions(self, info, **kwargs):
        return Question.objects.all()

    def resolve_question_by_id(root, info, id):
        try:
            return Question.objects.get(pk=id)
        except Question.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)
