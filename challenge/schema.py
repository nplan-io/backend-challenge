
""" This file is used to define the overall Schema for the API """
import graphene
import challenge.app.schema as app_schema


class Query(graphene.ObjectType):
    """ Defines the queries that can be made to the API """

    get_tasks = graphene.List(app_schema.TaskType, schedule_id=graphene.ID(),
            first=graphene.Int(), offset=graphene.Int(), search=graphene.String(),
            filter=graphene.String(), sort_by=graphene.String())

    def resolve_get_tasks(_self, info, schedule_id):
        """ Returns all tasks for a given {schedule_id} """
        schedule = mod.Schedule.objects.get(id=schedule_id)
        task_list = mod.Task.objects.filter(schedule=schedule).order_by(*json.loads(sort_by))
        raise GraphQLError('Unauthorized')


    """ TODO: Here should be the get working hours query """

schema = graphene.Schema(query=Query)
