menu={
    'Pizza':400,
    'Coffee':150,
    'Burger':150,
    'Salad':100,
    'Pasta':70,
}
print(f"Welcome to out resturant!")
print(f"1. Pizza : Rs300\n2. Coffee : 120\n3. Burger: 120\n4. Juice : 200\n5. Tea : 50\n6. Pasta : 150\n7. Salad:50\n")

total_amount = 0

item_1 = input(f"Enter the name of the item you want to order:")
if item_1 in menu:
    total_amount += menu[item_1]
    print(f"Your order {item_1} has been recieved !")
else:
    print(f"Sorry  {item_1}is not available yet!")
    
another_item = input(f"Would you like to order another item (Yes/No)")
if another_item == "Yes":
    item_2 = input("Enter the name of second item : ")
    if item_2 in menu:
        total_amount += menu[item_2]
        print(f"Your second order {item_2} has been recieved!")
        
    else:
        print("Sorry, {item_2}, item you have ordered is not available yet!")
print(f"The total amount of the item is : {total_amount}")