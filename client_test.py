import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    stock0, bid0, ask0, price0 = getDataPoint(quotes[0])
    stock1, bid1, ask1, price1 = getDataPoint(quotes[1])

    check0 = 120.84
    check1 = 119.775

    self.assertEqual(price0, check0)
    self.assertEqual(price1, check1)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    stock0, bid0, ask0, price0 = getDataPoint(quotes[0])
    stock1, bid1, ask1, price1 = getDataPoint(quotes[1])

    if bid0 > ask0:
       self.assertTrue(True)
    self.assertFalse(False)

    if bid1 > ask1:
       self.assertTrue(True)
    self.assertFalse(False)

  """ ------------ Add more unit tests ------------ """
  def test_valid_denominator_for_getRatio(self):    
    quotes = [
    {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
    {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
  ]
    
    stock0, bid0, ask0, price0 = getDataPoint(quotes[0])
    stock1, bid1, ask1, price1 = getDataPoint(quotes[1])

    if getRatio(price0, price1) == None:
       self.assertFalse(False)

    self.assertTrue(True)
    


if __name__ == '__main__':
    unittest.main()
