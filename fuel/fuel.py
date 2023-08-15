def main():


    check_fuel(get_percent())

def get_percent( ):
    while True:
        try:
            # Convert to integer
            fraction = input("Fraction: ").split('/')
            dividen = int(fraction[0])
            divisor = int(fraction[1])

            if dividen > divisor or divisor == 0:
                pass
            else:
                # Find the percent
                return f"{round((dividen/divisor)*100)}%"

        except  ZeroDivisionError:
            # print("Zero not divisible")
            pass
        except ValueError:
            # print("Incorrect Value")
            pass

def check_fuel(value):

    int_value = int(value.removesuffix("%"))
    if int_value <= 1:
        print("E")
    elif int_value >=99:
        print("F")
    else:
        print(value)

main()