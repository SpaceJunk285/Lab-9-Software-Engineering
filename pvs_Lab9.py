def encode(password):
    encoded = ""
    for i in str(password):
        encoded += str(int(i) + 3)
    return encoded

def decode(password):
    decoded = ""
    for char in password:
        new_char = str((int(char) - 3) % 10)
        decoded += new_char
    return decoded

if __name__ == '__main__':
    while True:
        print("Menu\n"
              "-------------\n"
              "1. Encode\n"
              "2. Decode\n"
              "3. Quit\n")

        option = int(input("Please enter an option:"))
        password = ""
        encoded = ""

        if option == 1:
            password = input("Please enter the password to encode:")
            encoded = encode(password)
            print("Your password has been encoded and stored!")

        elif option == 2:
            original_password = decode(encoded)
            print(f"The encoded password is {encoded}, and the original password is {password}.")

        elif option == 3:
            break
