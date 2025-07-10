from pandas.core.array_algos.transforms import shift

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


def encrypte():
    encrypte_form = ""
    for i in text:
        if i in alphabet:
            if alphabet.index(i) + shift > 25:
                encrypte_form = encrypte_form + alphabet[shift - 25 + alphabet.index(i) - 1]
            else:
                encrypte_form = encrypte_form + alphabet[alphabet.index(i) + shift]
        else:
            encrypte_form = encrypte_form + i

    print(encrypte_form)

def decrypt():
    decrypt_form = ""
    for i in text:
        if i in alphabet:
            if alphabet.index(i) - shift < 0:
                decrypt_form = decrypt_form + alphabet[25 - shift + alphabet.index(i) + 1]
            else:
                decrypt_form = decrypt_form + alphabet[alphabet.index(i) - shift]
        else:
            decrypt_form = decrypt_form + i
    print(decrypt_form)


while 1:

    direction = int(input("Type 1 to 'encode' to encrypt, type 2 to 'decode' to decrypt:\n"))
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == 1:
        encrypte()

    elif direction == 2:
        decrypt()

    elif direction == 3:
        break


