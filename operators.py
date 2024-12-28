def main():
    item_name = 'banana'
    quantity = 5
    discount_rate = 0.1
    eligible_items = "banana apple orange"
    item_price = 2

    subtotal = quantity * item_price

   # print(f"Item name: {item_name}, Subtotal is : {subtotal}")
    if item_name in eligible_items:
        discount = subtotal * discount_rate
    print(f"Item name is : {item_name} . applied discount is {discount}")

    was_discount_applied = discount > 0
    print(f"discount applied: {was_discount_applied}")

    #Logical Operators
    does_free_shipping = quantity >= 5 and item_name == 'banana'
    print(f"free shipping available: ? {does_free_shipping}")

    #price = subtotal - discount
    #print(f"Total price after discount: {price}")















if __name__ == '__main__':
    main()