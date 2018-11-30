
""" This file is used to define the overall Schema for the API """
import graphene
import graphql_jwt

import backendApi.app.schema as app_schema
import backendApi.users.schema as users_schema

class Query(app_schema.Query, users_schema.Query, graphene.ObjectType):
    """ Declares where the queries for the API are defined """

    pass

class Mutation(app_schema.Mutation, users_schema.Mutation, graphene.ObjectType):
    """ Declares where the mutations for the API are defined """

class Query(graphene.ObjectType):
    """ Defines the queries that can be made to the API """

    get_tasks = graphene.List(TaskType, schedule_id=graphene.ID(),
            first=graphene.Int(), offset=graphene.Int(), search=graphene.String(),
            filter=graphene.String(), sort_by=graphene.String())

    def resolve_get_tasks(_self, info, schedule_id):
        """ Returns all tasks for a given {schedule_id} """
            schedule = mod.Schedule.objects.get(id=schedule_id)
            task_list = mod.Task.objects.filter(schedule=schedule).order_by(*json.loads(sort_by))
        raise GraphQLError('Unauthorized')


    """ Here should be the get working hours query """

schema = graphene.Schema(query=Query, mutation=Mutation)
