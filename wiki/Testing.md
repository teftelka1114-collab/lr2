# Тестирование

Тесты написаны на unittest и лежат в каталоге `tests/`.

| Тест | Что проверяет |
|---|---|
| test_cart_total | сумма заказа в корзине |
| test_price_per_gb | цена за гигабайт памяти |
| test_price_per_gb_zero_memory | защита от деления на ноль |

Автозапуск: GitHub Actions, workflow `Tests` (при каждом push, pull request и вручную).
Локально: `python -m unittest discover -s tests -t . -v`
