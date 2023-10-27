""" ENTER A VALUE BELOW TO FIND HOW MANY CHARACTERS IT HAS"""

data = """The Gospel Changes Everything | 365"""

def main():
    total_chars = 0
    for count, char in enumerate(data):
        total_chars += 1
        print(count, char)

    print("  ")
    print(f"Total Characters: {total_chars}")
    print("  ")


if __name__ == "__main__":
    main()