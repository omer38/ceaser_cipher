alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def ceaser(start_text,shift_amount,cipher_direction):
    cipher_text=""
    if cipher_direction=="decode":
        shift_amount*=-1
    for letter in start_text:
        if letter in alphabet:
            position=alphabet.index(letter)
            new_position=position+shift_amount
            cipher_text+=alphabet[new_position]
        else:
            cipher_text+=letter
    print(f"{direction}ed text is {cipher_text}")

should_continue=True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift=shift%26
    ceaser(start_text=text,shift_amount=shift,cipher_direction=direction)

    result=input("Type yes if you want to go again. Otherwise no\n")
    if result=="no":
        should_continue=False
        print("Goodbye")
    elif result=="yes":
        should_continue=True















