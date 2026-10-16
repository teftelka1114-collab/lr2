"""Консольный прототип GPU Hub: каталог, фильтр и корзина."""
from gpu_hub.catalog import PRODUCTS, filter_by_vendor
from gpu_hub.cart import Cart


def show(products):
    for p in products:
        print(f"{p['id']}. {p['name']:<16} {p['vendor']:<7} {p['memory_gb']:>2} ГБ  {p['price']:>7} ₽")


if __name__ == "__main__":
    print("=== Каталог ===")
    show(PRODUCTS)
    print("\n=== Только AMD ===")
    show(filter_by_vendor("AMD"))

    cart = Cart()
    cart.add(2)
    cart.add(5)
    print(f"\nВ корзине 2 товара, итого: {cart.total()} ₽")
