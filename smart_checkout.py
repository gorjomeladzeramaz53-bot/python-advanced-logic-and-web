# ონლაინ მაღაზიის ჭკვიანი შეკვეთის და ფასდაკლების სისტემა (smart_checkout.py)

def process_checkout():
    print("🛒 ონლაინ მაღაზიის გადახდის სისტემა")
    
    # მონაცემების მიღება მომხმარებლისგან (ან შეგიძლიათ პირდაპირ ცვლადებში ჩაწეროთ)
    try:
        cart_total = float(input("შეიყვანეთ კალათის ღირებულება (ლარებში): "))
        user_status = input("შეიყვანეთ სტატუსი (regular, vip, admin): ").strip().lower()
        promo_input = input("გაქვთ აქტიური პრომოკოდი? (ki / ara): ").strip().lower()
        has_promo_code = True if promo_input == "ki" else False
        
        loyalty_points = float(input("შეიყვანეთ დაგროვილი ქულები: "))
        delivery_city = input("შეიყვანეთ მიტანის ქალაქი (მაგ: თბილისი, ბათუმი, რეგიონი): ").strip()
        
        active_input = input("არის თუ არა ანგარიში აქტიური? (ki / ara): ").strip().lower()
        is_account_active = True if active_input == "ki" else False

    except ValueError:
        print("❌ შეცდომა: გთხოვთ შეიყვანოთ სწორი რიცხვითი მონაცემები!")
        return

    # 1. ანგარიშის ვალიდაცია (Guard Clause)
    if not is_account_active:
        print("\n❌ [სისტემა]: ანგარიში დაბლოკილია. შეკვეთა ვერ დამუშავდება.")
        return

    # 2. კალათის მინიმალური ზღვარი
    if cart_total <= 0:
        print("\n❌ შეცდომა: კალათა ცარიელია ან მითითებულია არასწორი თანხა. შეკვეთა ვერ გატარდება.")
        return

    # 3. ფასდაკლებების სისტემა
    discount_percentage = 0.0

    if user_status == "vip":
        discount_percentage = 20.0
        # ჩაშენებული შემოწმება VIP-ისთვის
        if loyalty_points >= 500:
            discount_percentage += 5.0  # სულ 25%
            
    elif user_status == "regular":
        # ჩაშენებული შემოწმება Regular-ისთვის
        if has_promo_code or cart_total >= 150:
            discount_percentage = 10.0
        else:
            discount_percentage = 0.0
            
    elif user_status == "admin":
        discount_percentage = 50.0
    else:
        discount_percentage = 0.0

    # ფასდაკლებული თანხის გამოთვლა
    discount_amount = cart_total * (discount_percentage / 100)
    price_after_discount = cart_total - discount_amount

    # 4. მიტანის საფასურის გამოთვლა (in ოპერატორის გამოყენებით)
    major_cities = ["თბილისი", "ქუთაისი", "ბათუმი"]
    
    if delivery_city in major_cities:
        if price_after_discount >= 100:
            delivery_fee = 0.0
        else:
            delivery_fee = 5.0
    else:
        # რეგიონები
        delivery_fee = 15.0

    # საბოლოო გადასახდელი თანხა
    final_total = price_after_discount + delivery_fee

    # 5. საბოლოო რეპორტი (ინვოისი)
    print("\n" + "="*45)
    print("🧾 შეკვეთის დეტალური ინვოისი:")
    print(f"• კალათის საწყისი ფასი: {cart_total:.2f} ლარი")
    print(f"• მიღებული ფასდაკლება: {discount_percentage}% ({discount_amount:.2f} ლარი)")
    print(f"• თანხა ფასდაკლების შემდეგ: {price_after_discount:.2f} ლარი")
    print(f"• მიტანის საფასური ({delivery_city}): {delivery_fee:.2f} ლარი")
    print(f"• 💳 საბოლოო გადასახდელი თანხა: {final_total:.2f} ლარი")
    print("="*45)
    print("✅ შეკვეთა წარმატებით დამტკიცდა!")

if __name__ == "__main__":
    process_checkout()