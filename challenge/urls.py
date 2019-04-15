from django.contrib import admin
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

#from graphene_file_upload.django import FileUploadGraphQLView

from . import celery

def _celery_debug(request):
    """ A simple debug task to test Celery is functioning. """
    success = celery.debug_task.apply_async(args=[request.GET]).get()
    html = "<html><body>Celery Test: %s.</body></html>" % success
    return HttpResponse(html)

urlpatterns = [
    #url(r'^graphql', csrf_exempt(FileUploadGraphQLView.as_view(graphiql=True))),
    url('_celery_debug', _celery_debug)
]
