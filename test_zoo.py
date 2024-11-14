import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(0), 50)
        self.assertEqual(self.zoo.get_ticket_price(12), 50)
    
    # Add your additional test cases here.
    def test_teenager_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(13), 100)
        self.assertEqual(self.zoo.get_ticket_price(20), 100)

    def test_middle_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150)
        self.assertEqual(self.zoo.get_ticket_price(60), 150)

    def test_elderly_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 100)
    
    def test_invalid_age(self):
        self.assertIsNone(self.zoo.get_ticket_price(-1))

if __name__ == '__main__':
    unittest.main()