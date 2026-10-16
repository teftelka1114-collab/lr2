"""Каталог видеокарт."""

PRODUCTS = [
    {"id": 1, "name": "RTX 4060", "vendor": "NVIDIA", "memory_gb": 8, "price": 32990},
    {"id": 2, "name": "RTX 4070 Super", "vendor": "NVIDIA", "memory_gb": 12, "price": 69990},
    {"id": 3, "name": "RX 7600", "vendor": "AMD", "memory_gb": 8, "price": 29990},
    {"id": 4, "name": "RX 7800 XT", "vendor": "AMD", "memory_gb": 16, "price": 54990},
    {"id": 5, "name": "Arc B580", "vendor": "Intel", "memory_gb": 12, "price": 27990},
]


def get_product(product_id):
    """Вернуть товар по id или None, если такого нет."""
    for product in PRODUCTS:
        if product["id"] == product_id:
            return product
    return None


def filter_by_vendor(vendor):
    """Вернуть видеокарты выбранного производителя (регистр не важен)."""
    return [p for p in PRODUCTS if p["vendor"].lower() == vendor.lower()]


def price_per_gb(product):
    """Цена одного гигабайта видеопамяти (показатель выгодности)."""
    if product["memory_gb"] == 0:
        raise ValueError("Объём памяти не может быть нулевым")
    return product["price"] / product["memory_gb"]
