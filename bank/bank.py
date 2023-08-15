# Get user's greeting
greeting = input("Greeting: ").lower()

# Check user's greeting
if greeting.startswith("h") and not greeting.startswith("hello"):
    print("$20")
elif greeting.strip().startswith("hello"):
     print("$0")
else:
    print("$100")