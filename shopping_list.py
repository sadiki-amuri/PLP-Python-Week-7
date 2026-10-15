
while True:
    action = input("\nChoose an option (add / remove / show / done): ").strip().lower()
    
    if action == "add":
        item = input("Enter the item to add: ").strip()
        shopping_list.append(item)
        print(f" Added '{item}' to the list.")
        
    elif action == "remove":
        item = input("Enter the item to remove: ").strip()
        # Check it is actually in the list with 'in' before removing
        if item in shopping_list:
            shopping_list.remove(item)
            print(f" Removed '{item}' from the list.")
        else:
            print("That item is not on your list.")
            
    elif action == "show":
        print("--- Your Shopping List ---")
        # Print every item on its own line
        for item in shopping_list:
            print(item)
            
    elif action == "done":
        print("Thank you for using Shopping List Manager. Goodbye!")
        break
        
    else:
        print("Invalid option. Please type add, remove, show, or done.")
