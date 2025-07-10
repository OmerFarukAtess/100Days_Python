import  random
my_password = ""
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the password generator")
nr_letters = int(input("How many letters would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))

taken_nr_letters = 0
taken_nr_numbers = 0
taken_nr_symbols = 0


while len(my_password) < nr_letters + nr_numbers + nr_symbols:
    num = random.randint(0,2)
    if num == 0 and taken_nr_letters < nr_letters:
        taken_nr_letters += 1
        my_password += random.choice(letters)
    elif num == 1 and taken_nr_numbers < nr_numbers:
        taken_nr_numbers += 1
        my_password += random.choice(numbers)
    elif num == 2 and taken_nr_symbols < nr_symbols:
        taken_nr_symbols += 1
        my_password += random.choice(symbols)
        
print(my_password)