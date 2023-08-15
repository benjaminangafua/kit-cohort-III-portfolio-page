
name = ((input("File name: ")).lower().strip().split("."))[-1]

match name:
    case "jpg"|"jpeg":
        print("image/jpeg")
    case "txt":
        print("text/plain")
    case "png":
        print("image/png")
    case "gif":
        print("image/gif")
    case "pdf":
        print("application/pdf")
    case "zip":
        print("application/zip")
    case _:
        print("application/octet-stream")
