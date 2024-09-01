# Caesar Cipher
import string

alphabet = list(string.ascii_lowercase)

def caesar(original_text, shift_amount, encode_decode):
    output_text = ''
    for letter in original_text:
        if(letter in alphabet):
            index_original = alphabet.index(letter)
            shifted_position = 0
            if encode_decode == 'encode':
                shifted_position = index_original + shift_amount
            elif encode_decode == 'decode':
                shifted_position = index_original - shift_amount
            else:
                print(f"Type {encode_decode} doesn't exists!")
            
            # Prevent index of bound exception
            shifted_position %= len(alphabet)
            
            output_text += alphabet[shifted_position]
        else:
            output_text += letter
        
    print(f"Here is the {encode_decode}d result: {output_text}")
    
    



continue_game = True

while continue_game == True:
    encode_decode = input("Type 'encode' to encrypt, type 'decode' to decrypt: ") 
    text = input('Digit the text: ')
    shift_number = int(input('Type the shift number: '))

    caesar(original_text=text, shift_amount=shift_number, encode_decode=encode_decode)
    decision = input('Continue game? yes or no: ')
    
    if decision != 'yes':
        continue_game = False
        
    
    
    

