alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encryption(plain_text,shift_key):
    cipher_text=""
    for char in plain_text:
        position=alphabets.index(char)
        new_position=(position+shift_key)%26
        cipher_text+=alphabets[new_position]
    print(f"Here is the text after encryption: {cipher_text}")

def decryption(cipher_text,shift_key):
    plain_text=""
    for char in cipher_text:
        position=alphabets.index(char) 
        new_position=(position-shift_key)%26
        plain_text+=alphabets[new_position]
    print(f"Here is the text after encryption: {plain_text}")

want_end=False
while not want_end:
    what_to_do=input("Type encrypt for 'Encryption' or type decrypt for 'Decryption'")
    text=input("Enter your text \n")
    shift=int(input("Enter shift key:"))
    if what_to_do=="encrypt":
        encryption(plain_text=text,shift_key=shift)
    elif what_to_do=="decrypt":
        decryption(text,shift)
    
    play_again=input("Type 'Yes' to continue or type 'no' to exit\n").lower()
    if play_again=="no":
        want_end=True
        print("Thankyou for your response!!")
