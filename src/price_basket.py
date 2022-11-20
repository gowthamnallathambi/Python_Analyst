import sys


item_price = {'Soup':0.65, 'Bread':0.80, 'Milk':1.30, 'Apples':1.00}
discount = {'Apples':0.1, 'Bread':0.5}

class PriceBasket:
    def __init__(self, items):
        self.items = items             
        
    @property
    def items(self):
        return self._items
    
    @items.setter
    def items(self, items):
        if not isinstance(items, list):
            raise TypeError(f"{items} must be a list")
        if len(items) == 0:
            raise ValueError(f'No items in the list')        
        for item in items:
            if item not in item_price:
                raise ValueError(f'{item} item not in our inventory')
        self._items = items
        self._item_count = dict((x, self.items.count(x)) for x in set(self.items))
        
    @property
    def item_count(self):
        return self._item_count
    
        
    def __repr__(self):
        return f'PriceBasket({self.items})'
    
    def calculate_apple_discount(self):
        
        cnt = self.item_count['Apples']
        return cnt * discount['Apples']
    
    def calculate_bread_disconut(self):
        cnt = self._item_count['Bread']
        return (self.item_count['Soup'] // 2) * (discount['Bread'] * item_price['Bread'])#*(cnt//2)
    
    def calculate_subtotal(self):
        sub_total = 0           
        for item in self.items:
            sub_total += item_price[item]  
        return sub_total       
    
    
    def print_output(self):
        """_summary_
        Products that can be purchased, together with their prices are:
     
        Soup: 65p per tin.
        Bread: 80p per loaf.
        Milk: £1.30 per bottle.
        Apples: £1.00 per bag.
        Current special offers are as follows:
        
        Apples have a 10% discount off their normal price this week.
        Buy 2 tins of soup and get a loaf of bread for half price.
        """
        # sub_total = 0
        # total = 0        
        # # for item in self.items:
        # #     sub_total += item_price[item] 
        sub_total = self.calculate_subtotal()
        total =  sub_total
                
        print(f'Subtotal: £{sub_total:.2f}')
        #print(self._item_count)
        if 'Apples' in self._item_count:
            cnt = self.item_count['Apples']            
            total -= self.calculate_apple_discount()
            print(f"Apples {cnt*discount['Apples']*100}% off {cnt*discount['Apples']*100}p")
            
        if 'Soup' in  self._item_count and self.item_count['Soup'] >= 2 and 'Bread' in  self._item_count:
            cnt = self.item_count['Bread']
            total -= self.calculate_bread_disconut()
            print(f"Bread {discount['Bread']*100}% off {discount['Bread']*item_price['Bread']*100}p")
            
        else:
            print(f"(No offers available)")
             
        print(f'Total: £{total:.2f}')
        
 

if __name__=='__main__':
    n = len(sys.argv)
    items_list = []   
    if n < 1:
        print('commandline arguments missing')
        exit(0)
    elif sys.argv[1] != 'PriceBasket':
        print('First commandline argument PriceBasket missing')
        exit(0)
    elif n > 2 and sys.argv[1] == 'PriceBasket':
        for i in range(2, n):
            items_list.append(sys.argv[i])
        print(items_list)
        p = PriceBasket(items_list)
        p.print_output()
        
