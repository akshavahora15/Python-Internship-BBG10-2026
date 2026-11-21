def process_order(order):
    try:
        item = order["item"]
        price = order["price"]
    except KeyError as e:
        print(f"Error: Missing key {e}")
    else:
        print(f"Order details: {item} - Rs. {price}")
    finally:
        print("Processing complete")

process_order({"item": "Cake", "price": 500})
print("---")
process_order({"item": "Cake"}) 