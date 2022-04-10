import graphene
import CRUD_backend.schema




class Query(CRUD_backend.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)