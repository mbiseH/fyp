
import graphene
import CRUD_backend.schema


class Query(CRUD_backend.schema.Query, graphene.ObjectType):
    pass


class Mutation(CRUD_backend.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)