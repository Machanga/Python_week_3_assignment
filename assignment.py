def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price * ((100-discount_percent)/100)
        return final_price
    else:
        return price

price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount: "))

calculate_discount(price, discount_percent)