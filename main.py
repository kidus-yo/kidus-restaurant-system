#console based restaurant-system
running = True
food_cart = {"Hamburgers": 50,
             "Pizza": 60,
             "Chicken": 65,
             "French Fries": 20,
             "Club Sandwich": 33,
             "Beef Boleto": 30,
             "Chicken Lazaga": 44,
             "Beef Lazaga": 41,
             "Vegan Rice": 15,
             "Steaks": 70}

food_add = []
food_price = []

def main_menu():
   while running:

    print("Main Menu")
    print("1. Show food Menu")
    print("2. Take Order")
    print("3. View Cart")
    print("4. remove Item")
    print("5. Checkout")
    print("6. Clear Cart")
    print("7. Exit❎")
     
    choice = int(input("Please Enter your choice?: "))
    if choice == 7:
       running == False
       print("Thank you!Come again😁")
       break
    return choice
    

def food_menu():
    print("Kidus Restaurnt Menu:")
    print("1. Hamburgers🍔..........$50.00")
    print("2. Pizza🍕...............$60.00")
    print("3. Chicken🍗.............$65.00")
    print("4. French Fries🍟........$20.00")
    print("5. Club Sandwich🥪.......$33.00")
    print("6. Beef Boleto🌯.........$30.00")
    print("7. Chicken Lazaga🥘......$44.00")
    print("8. Beef Lazaga.🍲........$41.00")
    print("9. Vegan Rice🍚..........$15.00")
    print("10. Steaks🥩.............$70.00")

def take_order():
    order = input("What food would you like to order?: ")
    if order in food_cart:
        food_add.append(order)
        food_price.append(food_cart[order])
        print(f"{order} added Sucessfully in the cart!✅")
    else:
       print(f"{order} not found in the main menu")
    
def view_cart():
   for food in food_add:
      for price in food_price:
         print() 
def main():
   choice = main_menu()
   if choice == 1:
    food_menu()
   elif choice == 2:
       take_order()
   elif choice == 3:
      pass
main()