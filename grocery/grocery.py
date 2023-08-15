

grocery_list = {}
while True:
    try:

        user_item = input("").upper()

        if grocery_list.get(user_item) == None:
            grocery_list[user_item] = 1
        else:
            grocery_list[user_item] += 1

    except  (KeyboardInterrupt, EOFError) :
        print()
        sorted = sorted(grocery_list.items())
        for item, num in sorted:
            print(num, item)

        break


