def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b


while True:
    print("1) add")
    print("2) sub")
    print("3) mul")
    print("4) div")
    print("0) exit")

    choice = input("choice: ")

    if choice == "0":
        print("Bye!")
        break

    if choice in ("1", "2", "3", "4"):
        a = int(input("a: "))
        b = int(input("b: "))

        if choice == "4" and b == 0:
            print("Cannot divide by zero. Exiting...")
            break  # ← 設計どおり「強制終了」

        if choice == "1":
            result = add(a, b)
        elif choice == "2":
            result = sub(a, b)
        elif choice == "3":
            result = mul(a, b)
        else:
            result = div(a, b)

        print(f"result: {result}")
    else:
        print("Invalid choice")
