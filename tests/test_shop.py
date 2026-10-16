import unittest

from gpu_hub.cart import Cart
from gpu_hub.catalog import get_product, price_per_gb


class ShopTests(unittest.TestCase):
    def test_cart_total(self):
        """Сумма корзины: RTX 4070 Super (69990) + 2 x RX 7600 (29990)."""
        cart = Cart()
        cart.add(2)
        cart.add(3, qty=2)
        self.assertEqual(cart.total(), 69990 + 2 * 29990)

    def test_price_per_gb(self):
        """RX 7800 XT: 54990 ₽ / 16 ГБ = 3436,875 ₽ за гигабайт."""
        self.assertAlmostEqual(price_per_gb(get_product(4)), 3436.875)

    def test_price_per_gb_zero_memory(self):
        """Нулевой объём памяти приводит к ошибке, а не к делению на ноль."""
        with self.assertRaises(ValueError):
            price_per_gb({"name": "Test", "memory_gb": 0, "price": 1000})


if __name__ == "__main__":
    unittest.main()
