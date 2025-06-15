# 복잡한 데이터 변환
sales_data = [{'product': 'A', 'quantity': 10, 'price': 100},
              {'product': 'B', 'quantity': 20, 'price': 200},]
total_revenue = sum(item['quantity'] * item['price'] for item in sales_data)

print(f"total_revenue: {total_revenue}")