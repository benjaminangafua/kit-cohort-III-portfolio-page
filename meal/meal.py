# Get meal time

time = input("What time is it? ")


def main():
    timeFormat  = convert(time)

    if 8 >= timeFormat >= 7:
        print("breakfast time")
    elif 12 <=timeFormat <= 13:
        print("lunch time")
    elif 19>= timeFormat >=18:
        print("dinner time")

def convert(time):
    hour,minutes = time.split(":")

    return (float(hour)+ (float(minutes))/60)

if __name__ == "__main__":
    main()
