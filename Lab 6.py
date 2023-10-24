global password
# This function encodes passwords.
def encode(p):
    temp = ""
    for i in p:
        temp += str((int(i) + 3) % 10)
    return temp

# David's Decode function
def decode(encoded_passsword):
    final_password = ""

    #Iterate through each integer in the the encoded password and decode it and add to final password
    for value in encoded_passsword:
        new_value = int(value) + 7
        final_password += str(new_value%10)
    
    return final_password
    
if __name__ == "__main__":
    # This is where the menu is stored and choices are handled.
    while True:
        print("Menu")
        print("------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print("")
        print("Please enter an option: ")
        choice = int(input())
        if choice == 1:
            print("Please enter your password to encode: ", end = "")
            password = encode(input())
            print("Your password has been encoded and stored!")
        if choice == 2:
            print("The encoded password is " + str(password) + ", and the original password is " + decode(password) + ".")
        if choice == 3:
            break
