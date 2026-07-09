#console based restaurant-system
running = True
#Dictionary
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

#list as a cart
food_add = []
food_price = []
 
 #FUNCTION for the main menu
def main_menu():
    print("Main Menu")
    print("1. Show food Menu")
    print("2. Take Order")
    print("3. View Cart")
    print("4. remove Item")
    print("5. Clear Cart")
    print("6. Exit❎")
     
    choice = int(input("Please Enter your choice?: "))
    return choice
 
 #Function for the food Menu   
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

#Function to take order
def take_order():
    order = input("What food would you like to order?: ")
    if order in food_cart:
        food_add.append(order)
        food_price.append(food_cart[order])
        print(f"{order} added Sucessfully in the cart!✅")
    else:
       print(f"{order} not found in the main menu")

#Function to see what is added and remived    
def view_cart():
   for food in food_add:
         price = food_cart[food]
         print(f"{food}......${price}") 
#Function to remove an item
def remove_item():
   remove = input("What item would u like to remove form the cart?: ")
   if remove in food_cart:
    index = food_add.index(remove)
    food_add.pop(index)
    food_price.pop(index)
    print(f"{remove} removed successfully form the cart!🛒✅")
   else:
      print(f"{remove} not found in the cart🛒❌")    

#Function to clear cart
def clear_cart():
   food_add.clear()
   food_price.clear()
   print("Cart🛒 cleared successfully!✅")      
#Main function that holds every other function
def main():
 while True:
   choice = main_menu()
   if choice == 1:
    food_menu()
   elif choice == 2:
       take_order()
   elif choice == 3:
     view_cart()
   elif choice == 4:
      remove_item()
   elif choice == 5:
      view_cart()
   elif choice == 6:
      
      print("Thank you! Come again😁") 
      break
      
   else:
      print("Invalid Choice❌Please try again")

main()