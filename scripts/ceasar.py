import string
import optparse

print("##################################################")
print("#       Ceasar Cipher encode/decode tool         #")
print("##################################################")
print("@rubb3rsc4nm4n")

def get_arguments():
    parser= optparse.OptionParser()
    parser.add_option("-s", "--shift", dest="shift", help="Enter the shift value you would like to use in your cipher")
    parser.add_option("-d", "--decode", dest="method", help="Flag used for decoding, encoding requires no flag")
    parser.add_option("-m", "--message", dest="message", help="enter the ciphertext or clear text")
    (options, arguments) = parser.parse_args()
    if not options.message:
        print("Please input a message to encode/decode")
    elif not options.shift:
        print("Please specify a shift value as an integer")
    else:
        return options
    
def parse_lists(message, shift):    
    message_list = []
    ascii_reference = string.ascii_lowercase
    ascii_list = []
    char_list = []
    
    ## split ascii string into searchable list
    for char in message:
        message_list.append(char)

    for char in ascii_reference:
        ascii_list.append(char)

    ## split example string into searchable list
    for char in ascii_reference:
        char_list.append(char)
    for char in ascii_reference:
        char_list.append(char)

    ## for decryption, you have to reverse the order of the list and make it double
    ## length to account for first shift num of characters
    #ascii_list = reversed(ascii_list)
    #for i in ascii_list:
    #    ascii_list.append(i)
        
    dec_length = 26-shift
    end = 52-shift
    
    decrypt_list = char_list[dec_length:end]
    
    enc_length = 26 + shift
    start = shift
    encrypt_list = char_list[start:enc_length]

    list_of_lists = [message_list, ascii_list, encrypt_list, decrypt_list]

    return list_of_lists
    ## loop through characters in example_list, find the index of each letter in 
    ## ascii_list and shift it by 2, then append each character to the answer 
    ## string. To avoid out of range index, make special cases for 'y' and 'z'
    

def decrypt(character_list, message_list, ascii_list):
    cleartext = ""
    for i in message_list:
        if i != " ":
            new_index = ascii_list.index(i)
            new_char = character_list[new_index]
            cleartext += new_char
        else:
            new_char = i
            cleartext += new_char
    return cleartext
 
    ## loop through characters in example_list, find the index of each letter in 
    ## ascii_list and shift it by 2, then append each character to the answer 
    ## string. To avoid out of range index, make special cases for 'y' and 'z'
def encrypt(character_list, message_list, ascii_list):
    ciphertext = ""
    for i in message_list:
        if i != " ":
            new_index = ascii_list.index(i)
            new_char = character_list[new_index]
            ciphertext += new_char
        else:
            new_char = i
            ciphertext = ciphertext + new_char
    return ciphertext
    
    
options = get_arguments()
shift = int(options.shift)
ceasar_lists = parse_lists(options.message, shift)
if not options.method:
    cipher_text = encrypt(ceasar_lists[2], ceasar_lists[0], ceasar_lists[1])
    print("Ciphertext:")
    print(cipher_text)
else:
    clear_text = decrypt(ceasar_lists[3], ceasar_lists[0], ceasar_lists[1])
    print("Cleartext:")
    print(clear_text)




















