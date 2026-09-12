import unittest
from src.orders import record_order


class SmokeTests(unittest.TestCase):
    def test_new_order(self):
        orders = {}
        result = record_order(orders, "a", {"qty": 2})
        self.assertEqual(result, {"qty": 2})
        self.assertEqual(orders["a"], result)

    def test_empty_key(self):
        with self.assertRaises(ValueError):
            record_order({}, "", {})


if __name__ == "__main__":
    unittest.main()
