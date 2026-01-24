print("\nLab Problem 1: Data Analysis System")
print("=" * 50)

# Sample sales data: A list of dictionaries
# This structure is common when working with databases or CSV imports
sales_data = [
    {"product": "Laptop", "category": "Electronics",
        "price": 999.99, "quantity": 5, "region": "North"},
    {"product": "Mouse", "category": "Electronics",
        "price": 29.99, "quantity": 20, "region": "North"},
    {"product": "Keyboard", "category": "Electronics",
        "price": 79.99, "quantity": 15, "region": "South"},
    {"product": "Monitor", "category": "Electronics",
        "price": 299.99, "quantity": 8, "region": "North"},
    {"product": "Desk", "category": "Furniture",
        "price": 199.99, "quantity": 3, "region": "South"},
    {"product": "Chair", "category": "Furniture",
        "price": 149.99, "quantity": 7, "region": "North"},
    {"product": "Lamp", "category": "Furniture",
        "price": 49.99, "quantity": 12, "region": "South"},
    {"product": "Book", "category": "Education",
        "price": 19.99, "quantity": 50, "region": "North"},
    {"product": "Pen", "category": "Education",
        "price": 2.99, "quantity": 100, "region": "South"},
]

print("Sales Data Analysis")
print("-" * 30)

# 1. Calculate total revenue by category
category_revenue = {}
for item in sales_data:
    category = item["category"]
    revenue = item["price"] * item["quantity"]
    # Safely building the dictionary using .get()
    category_revenue[category] = category_revenue.get(category, 0) + revenue

print("Revenue by category:")
# Sorting categories by revenue amount (x[1])
for category, revenue in sorted(category_revenue.items(), key=lambda x: x[1], reverse=True):
    print(f"  {category}: ${revenue:,.2f}")

# 2. Find products with highest total value (Dictionary Comprehension)
product_values = {item["product"]: item["price"] * item["quantity"]
                  for item in sales_data}
top_products = sorted(product_values.items(),
                      key=lambda x: x[1], reverse=True)[:3]

print(f"\nTop 3 products by total value:")
for product, value in top_products:
    print(f"  {product}: ${value:,.2f}")

# 3. Regional analysis (Using nested dictionaries and sets)
regional_sales = {}
for item in sales_data:
    region = item["region"]
    if region not in regional_sales:
        # Initializing the sub-dictionary
        regional_sales[region] = {"revenue": 0, "products": set()}

    regional_sales[region]["revenue"] += item["price"] * item["quantity"]
    # Sets automatically ensure we only count unique products
    regional_sales[region]["products"].add(item["product"])

print(f"\nRegional analysis:")
for region, data in regional_sales.items():
    print(
        f"  {region}: ${data['revenue']:,.2f} revenue, {len(data['products'])} unique products")

# 4. Price range analysis (List Comprehensions)
prices = [item["price"] for item in sales_data]
price_ranges = {
    "Under $50": len([p for p in prices if p < 50]),
    "$50-$100": len([p for p in prices if 50 <= p < 100]),
    "$100-$500": len([p for p in prices if 100 <= p < 500]),
    "Over $500": len([p for p in prices if p >= 500])
}

print(f"\nPrice range distribution:")
for range_name, count in price_ranges.items():
    print(f"  {range_name}: {count} products")
