import graphene
from graphene_django import DjangoObjectType

from api.models.program import YoungCoder
from api.schemas.common import DifficultyNode, ImageUrl


class YoungCoderNode(DjangoObjectType):
    class Meta:
        model = YoungCoder
        description = """
        YoungCoder
        """

    difficulty = graphene.Field(DifficultyNode)
    company_logo = graphene.Field(ImageUrl)


class Mutations(graphene.ObjectType):
    pass


class Query(graphene.ObjectType):
    youngCoders = graphene.List(YoungCoderNode)
    youngCoder = graphene.Field(YoungCoderNode, id=graphene.Int())

    def resolve_young_coders(self, info):
        return YoungCoder.objects.filter(visible=True, accepted=True)

    def resolve_young_coder(self, info, id):
        return YoungCoder.objects.get(pk=id, accepted=True)