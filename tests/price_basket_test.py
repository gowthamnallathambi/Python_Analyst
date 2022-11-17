import unittest

from src.price_basket import PriceBasket,item_price, discount

class TestPriceBasket(unittest.TestCase):
    
    def test_create_price_basket_with_out_list(self):
        with self.assertRaises(TypeError):
            pb = PriceBasket(2)
            
    def test_create_price_basket_with_wrong_item(self):
        with self.assertRaises(ValueError):        
            pb = PriceBasket(['Apple'])
            
    def test_create_price_basket_with_empty_items(self):
        with self.assertRaises(ValueError):        
            pb = PriceBasket([])
            
    def test_apple_discount(self):
        p = PriceBasket(['Apples'])
        d = p.calculate_apple_discount()
        cnt = p.item_count['Apples']
        self.assertEqual(d , cnt*discount['Apples'])
        
   
    def test_subtotal(self):
        cnt = 0
        items = ['Apples', 'Apples','Milk', 'Bread']
        p = PriceBasket(items)
        subtotal_ = 0
        for item in items:
            subtotal_ += item_price[item]  
        subtotal = p.calculate_subtotal()    
        self.assertEqual(subtotal, subtotal_)
