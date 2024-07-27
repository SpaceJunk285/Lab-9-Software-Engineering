def encode(password):
    encoded = ""
    for i in str(password):
        encoded += str(int(i) + 3)
    return encoded


def decode(password):
    decoded_password = ""
    for char in password:
        new_char = str((int(char) - 3) % 10)
        decoded_password += new_char
    return decoded_password

if __name__ == '__main__':
    password_in = ""
    encoded_pass = ""

    while True:
        print("Menu\n"
              "-------------\n"
              "1. Encode\n"
              "2. Decode\n"
              "3. Quit\n")

        option = int(input("Please enter an option: "))

        if option == 1:
            password_in = input("Please enter the password to encode: ")
            encoded_pass = encode(password_in)
            print("Your password has been encoded and stored!\n")

        elif option == 2:
            original_password = decode(encoded_pass)
            print(f"The encoded password is {encoded_pass}, and the original password is {original_password}.\n")


        elif option == 3:
            break
