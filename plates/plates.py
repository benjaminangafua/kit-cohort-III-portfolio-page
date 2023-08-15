def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    # Convert a user’s input to uppercase
    s = s.upper()

    # contain a minimum of 2 and a maximum of 6 characters (letters or numbers)
    if 2<= len(s) <= 6:

        # No periods, spaces, or punctuation marks are allowed.
        if s.isalnum():

            # must start with at least two letters
            if s[0:2].isalpha():
                # print(s)
                if valid_num(s):
                    return s
def valid_num(num):

    nums = []
    iterate = 1
    for i in range(len(num)):

        # When the numbers begin with `0` print invalid
        if num[i].isdigit():
            nums.append(num[i])

        if nums != []:
            if nums[0] == "0":
                return False

        # If all are letters
        elif num.isalpha():
            return num

        # Check for number in middle of letters
        else:
            rn = ""
            for j in range(len(num) -2):
                # Get the set of three strings
                rn = num[j:j+3]
                st = rn[0].isdigit()
                nd = rn[1].isalpha()
                rd = rn[2].isdigit()

                # Check for the strings pattern correctly
                if rn[0].isalpha() and rn[1].isalpha() and rn[2].isdigit():
                    continue
                elif st and nd and rd:
                   return
        iterate += iterate
    return num
main()