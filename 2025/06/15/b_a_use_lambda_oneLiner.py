# 람다 함수 활용
price_after_discount = lambda price: price - price * 0.9
tax_calc = lambda amount, rate = 0.1: amount * (1 + rate)

print(f"price_after_discount: {price_after_discount(10000)}")
print(f"tax: {tax_calc(price_after_discount(10000))}")