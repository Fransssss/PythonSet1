# set = unordered and unindexed collection. no duplicate value

randThings = {"Table", "chair", "house", "shoes", "stove"}
furniture = {"Table", "mirror", "chair", "couch", "stove"}

# randThings.clear()
# randThings.pop()
# randThings.remove()
# randThings.add()
# randThings.difference(furniture)
# randThings.union(furniture)

print("\n== DataSet Menu ==")
print("1. Display data")
print("2. Add an item")
print("3. Remove an item")
print("4. Take out last item")                                #take out whatever item in the last index
print("5. Clear data")
print("6. The difference between data")
print("7. The union between data")                            # item/s that exist in both data
print("8. Join the data")
print("E. Exit")
choice = input("choice: ")

while choice != 'e' and choice != 'E':
    if choice == "1":
        print("\nDisplay data")
        print("Random things: " + str(randThings))
        print("Furniture: " + str(furniture))
    elif choice == "2":
        print("\nAdd an item")
        data = input("a.1st dataset\nb.2nd dataset\nwhich dataset you'd like to add an item to: ")
        if data == 'a':
            item = input("input name of new item: ")
            randThings.add(item)
            print("item added")
        elif data == 'b':
            item = input("input name of new item: ")
            furniture.add(item)
            print("item added")
        else:
            print("[invalid choice]")
    elif choice == "3":
        print("\nRemove an item")
        data = input("a.1st dataset\nb.2nd dataset\nwhich dataset you'd like to remove an item from: ")
        if data == 'a':
            remv = input("input the name of item to remove: ")
            randThings.remove(remv)
            print("item has been removed")
        elif data == 'b':
            remv = input("input the name of item to remove: ")
            furniture.remove(remv)
            print("item has been removed")
        else:
            print("[invalid choice]")
    elif choice == "4":
        print("\nTake out last item")
        data = input("a.1st dataset\nb.2nd dataset\nwhich dataset you'd like to remove its last item: ")
        if data == 'a':
            randThings.pop()
            print("last item has been removed")
        elif data == 'b':
            furniture.pop()
            print("last item has been removed")
    elif choice == "5":
        print("\nClear data")
        data = input("a.1st dataset\nb.2nd dataset\nwhich dataset you'd like to clear its dataset: ")
        if data == 'a':
            randThings.clear()
            print("dataset has been cleared")
        elif data == 'b':
            furniture.clear()
            print("dataset has been cleared")
        else:
            print("[invalid choice]")
    elif choice == "6":
        print("\nThe difference between data")
        print(randThings.difference(furniture))              # or otherwise
    elif choice == "7":
        print("\nThe union between data")
        print(randThings.intersection(furniture))
    elif choice == "8":
        print("\nJoin the data")
        print(randThings.union(furniture))
    else:
        print("\n[Invalid choice]")

    print("\n== Set Menu ==")
    print("1. Display data")
    print("2. Add an item")
    print("3. Remove an item")
    print("4. Take out last item")  # take out whatever item in the last index
    print("5. Clear data")
    print("6. The difference between data")
    print("7. The union between data")  # item/s that exist in both data
    print("8. Join the data")
    print("E. Exit")
    choice = input("choice: ")

if choice == 'e' or choice == 'E':
    print("\n== Exit Program ==")


