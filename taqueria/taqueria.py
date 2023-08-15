
def main():
    item = getDicItem()
    order = getOrder("Item: ", item)
    printTotal(order)

def getDicItem():
    return dict({
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
        })

def getOrder(prompt, item):
    total = 0
    while True:
        try:
            user_input = prompt_user(prompt)
            try:
                if user_input in item:
                    total += item[user_input]
                    printTotal(total)

            except KeyError:
               user_input = prompt_user(prompt)
        except (KeyboardInterrupt, EOFError) :
            print()
            return total

# Find order in menu

def prompt_user(prompt):
    return input(prompt).title()


def printTotal(total):
    print(f"Total ${total:.2f}")


main()

