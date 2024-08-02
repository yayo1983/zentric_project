from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from products.infrastructure.models import Product

def assign_permissions():
    # Get the content type for the Product model
    content_type = ContentType.objects.get_for_model(Product)

    # Obtaining permits
    view_permission = Permission.objects.get(
        codename="view_product2", content_type=content_type
    )
    edit_permission = Permission.objects.get(
        codename="edit_product2", content_type=content_type
    )
    print("permisos a asignar: ")
    print(view_permission, edit_permission)

    # Assign permissions to a specific user
    user = User.objects.get(username="carlos")
    user.user_permissions.add(view_permission, edit_permission)

    print(f"Permissions assigned to {user.username}")

assign_permissions()
