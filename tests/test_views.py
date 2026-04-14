from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import MenuItem
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):

    def setUp(self):
        self.client = APIClient()

        self.item1 = MenuItem.objects.create(
            title="Burger",
            price=5.99,
            inventory=10
        )
        self.item2 = MenuItem.objects.create(
            title="Pasta",
            price=7.99,
            inventory=8
        )

    def test_get_all_menu_items(self):
        response = self.client.get('/restaurant/menu/items/')  # adjust URL if needed

        menus = MenuItem.objects.all()
        serializer = MenuSerializer(menus, many=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)