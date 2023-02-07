from unittest import TestCase

from starter_code.models.item import ItemModel

class ItemTest(TestCase):

    def test_create_item(self):
        item = ItemModel("pc", 1500)

        self.assertEqual("pc", item.name)
        self.assertEqual(1500, item.price)

    def test_item_json(self):
        item = ItemModel("pc", 1500)
        expected = {
            "name" : "pc",
            "price": 1500,
        }
        self.assertEqual(item.json(), expected)