from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from graphene_django.views import GraphQLView

class PrivateGraphQLView(GraphQLView):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
