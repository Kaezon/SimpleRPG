"""
Project-level schema File
"""
import graphene
import base.schema
from base.schema import BaseMutations

class Query(base.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=BaseMutations)
