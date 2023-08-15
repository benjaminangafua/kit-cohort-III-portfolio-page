months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    try:
        convertDate()
    except:
        print("Error")


def user_date_list():
    while True:
        date =input("Date: ").strip()

        if "," in date:
            (month, day, year) = (date.replace(",","")).split()
            # Advoiding Date like: 17 April, 2023
            if(day not in months):
                if (0 < int(day) <= 31) and (0< months.index(month)+1 <=12):
                    return (month, day, year)
        elif "/" in date:
            (month, day, year) = date.split("/")

            # Advoiding Date like: April/17/2023
            if not month in months:
                if 0 < int(day) <= 31 and 0< int(month) <=12:

                    return (month, day, year)

def convertDate():
    (month, day, year) =user_date_list()

    """
    String of a month: Convert the day to int and find the index of the month
    """
    if month in months:
        if 0 < int(day) <= 31:
            day_num = f"{int(day):02}"
            month_num = f"{months.index(month)+1:02}"

        print(f"{year}-{month_num}-{day_num}")
    else:
        print(f"{year}-{int(month):02}-{int(day):02}")

main()