from django.contrib import admin
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from graphene_file_upload import ModifiedGraphQLView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^graphql', csrf_exempt(ModifiedGraphQLView.as_view(graphiql=True))),
]
