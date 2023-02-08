# There is an implementation of the Product class in the product.py file and an implementation of the ShoppingBasket class in the basket.py file.
# In the solution file (exercise.py), create a TestBasketWithOneProduct class that inherits from unittest.TestCase. Add a setUpClass() class method that creates an instance of the ShoppingBasket class and assigns it as an attribute of the TestBasketWithOneProduct test class named basket. Add one product with the following parameters to the instance created in this way:
# name='milk', price=3.0
# Implement the following test methods for a single-product basket in the TestBasketWithOneProduct class:
# test_size_of_basket_should_be_one() - checks if basket size is equal to 1
# test_total_amount_should_have_tax() - checks if the total value of the cart is 3.63
# test_getting_product() - checks if the product name with index 0 is 'milk' -> use the get_product() method for this
# test_getting_product_out_of_range_should_raise_error() - checks if we get an IndexError when trying to read a product with index 1
# All you need to do is define the class and the appropriate tests. During the verification of the solution, the tests are run and in the event of any errors, the test report will be printed to the console.


from unittest import TestCase
from basket import ShoppingBasket
from product import Product

class TestBasketWithNoProducts(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.basket = ShoppingBasket()

    def test_size_of_basket_should_be_empty(self):
        result = len(self.basket)
        expected = 0
        self.assertEqual(result, expected)
    
    def test_getting_product_out_of_range_should_raise_error(self):
        with self.assertRaises(IndexError):
            self.basket.get_product(0)
    def test_total_amount_should_be_zero(self):
        result = self.basket.total()
        expected = 0
        self.assertEqual(result, expected)

class TestBasketWithOneProduct(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.basket = ShoppingBasket()
        cls.basket.add_product("milk", 3.0)

    def test_size_of_basket_should_be_one(self):
        self.assertEqual(len(self.basket), 1)

    def test_total_amount_should_have_tax(self):
        self.assertEqual(self.basket.total(), 3.63)
    
    def test_getting_product(self):
        result = self.basket.get_product(0).name
        expected = "milk"
        self.assertEqual(result, expected)
    def test_getting_product_out_of_range_should_raise_error(self):
        self.assertRaises(IndexError, self.basket.get_product, 1)
    

    

    


        





        
