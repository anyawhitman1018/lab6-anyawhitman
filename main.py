# Anya Whitman (encode function)
# Tavienne Millner (decode function)


# Encode function.
def encode(password_to_encode):
    # List to help the encode process.
    password_chars_encoded = []

    for char in password_to_encode:
        password_chars_encoded.append(str(int(char) + 3))
    print("Your password has been encoded and stored!")

    return password_chars_encoded


# Main function.
def main():

    # A while loop so the program runs until the user chooses to stop.
    while True:

        print("""Menu
-------------
1. Encode
2. Decode
3. Quit""""")
        user_input = input("Please enter an option: ")

        # If/else logic depending on the user's input.
        if user_input == "1":
            # Gets user's password to encode.
            password_to_encode = input("Please enter your password to encode: ")

            # List of encoded characters.
            password_chars_encoded = encode(password_to_encode)

            # Creating the encoded password string.
            encoded_password = ""
            for char in password_chars_encoded:
                encoded_password += char[-1]

        elif user_input == "2":
            pass

        # Exits program
        elif user_input == "3":
            exit()


# Calls the main function.
if __name__ == "__main__":
    main()



