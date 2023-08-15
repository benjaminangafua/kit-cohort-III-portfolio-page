def main():

    face = (input(""))
    convert(face)


def convert(userContent):
    for feeling in ((":)", "🙂"), (":(", "🙁")):
        userContent = userContent.replace(*feeling)
    print(userContent)

main()