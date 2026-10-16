"""Корзина покупателя."""
from gpu_hub.catalog import get_product


class Cart:
    def __init__(self):
        self.items = {}  # id товара -> количество

    def add(self, product_id, qty=1):
        if get_product(product_id) is None:
            raise ValueError(f"Товар {product_id} не найден")
        if qty < 1:
            raise ValueError("Количество должно быть положительным")
        self.items[product_id] = self.items.get(product_id, 0) + qty

    def total(self):
        """Итоговая сумма заказа в рублях."""
        return sum(get_product(pid)["price"] * qty for pid, qty in self.items.items())
