from django.contrib import admin
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from graphene_file_upload.django import FileUploadGraphQLView

urlpatterns = [
    url(r'^graphql', csrf_exempt(FileUploadGraphQLView.as_view(graphiql=True))),
]
