from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from graphene_django.views import GraphQLView

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from graphene_django.views import GraphQLView

class PrivateGraphQLView(GraphQLView):
    """
    Custom GraphQL view that requires user authentication to access.

    This class inherits from the `GraphQLView` provided by `graphene-django` and uses the `login_required` decorator
    to enforce that the user must be logged in to access any GraphQL queries or mutations. If the user is not authenticated,
    they will be redirected to the login page.

    Methods:
    - dispatch: Overrides the default `dispatch` method to apply the `login_required` decorator, ensuring that only authenticated
      users can access the GraphQL endpoint. The decorator redirects unauthenticated users to the login page.
    """
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        """
        Handle the HTTP request.

        This method applies the `login_required` decorator to enforce authentication. It then calls the parent class's
        `dispatch` method to handle the request as usual, processing GraphQL queries or mutations.

        Args:
            *args: Positional arguments for the parent `dispatch` method.
            **kwargs: Keyword arguments for the parent `dispatch` method.

        Returns:
            The result of the parent class's `dispatch` method, which processes the GraphQL request.
        """
        return super().dispatch(*args, **kwargs)

