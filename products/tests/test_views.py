from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User, Group, Permission
from products.infrastructure.models import Product


class ProductAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        
        self.create_permissions()

        product_group = Group.objects.create(name="test group")
        add_product_permission = Permission.objects.get(codename="add_product")
        view_product_permission = Permission.objects.get(codename="view_product")
        edit_product_permission = Permission.objects.get(codename="edit_product")
        delete_product_permission = Permission.objects.get(codename="delete_product")
        product_group.permissions.add(
            add_product_permission,
            view_product_permission,
            edit_product_permission,
            delete_product_permission,
        )

        self.user.groups.add(product_group)
        self.product = Product.objects.create(name="Test Product", price=100.0, user=self.user)
        
        self.client.force_authenticate(user=self.user)
        
        self.url = reverse("product-list-create")
        
    def create_permissions(self):
        if not Permission.objects.filter(codename='add_product').exists():
            Permission.objects.create(
                codename='add_product',
                name='Can add product',
                content_type_id=Product._meta.app_label
            )
        if not Permission.objects.filter(codename='view_product').exists():
            Permission.objects.create(
                codename='view_product',
                name='Can view product',
                content_type_id=Product._meta.app_label
            )


    # def test_list_products(self):
    #     response = self.client.get(self.url)
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(len(response.data), 1)

    # def test_create_product(self):
    #     data = {'name': 'New Product', 'price': 200.0}
    #     response = self.client.post(self.url, data)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(Product.objects.count(), 2)
    #     self.assertEqual(Product.objects.get(id=response.data['id']).name, 'New Product')

    # def test_retrieve_product(self):
    #     url = reverse('product-detail', args=[self.product.id])
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data['name'], self.product.name)

    # def test_update_product(self):
    #     url = reverse('product-detail', args=[self.product.id])
    #     data = {'name': 'Updated Product', 'price': 150.0}
    #     response = self.client.put(url, data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.product.refresh_from_db()
    #     self.assertEqual(self.product.name, 'Updated Product')

    # def test_delete_product(self):
    #     url = reverse('product-detail', args=[self.product.id])
    #     response = self.client.delete(url)
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    #     self.assertEqual(Product.objects.count(), 0)
