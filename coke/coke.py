def main():
    get_coin()

def get_coin():
    print("Amount Due: 50")
    coin = 0
    while True:
        insert = int(input("Insert Coin: "))
        if insert == 25 or insert == 10 or insert == 5:

            # Track coins
            coin +=  insert
            change = 50 - coin
            if coin < 50:
                print(f"Amount Due: {change}")
            else:
                # Return change owed
                owed = change * - 1
                print(f"Change Owed: {owed}")
                break
        else:
            print(f"Amount Due: 50")
main()

