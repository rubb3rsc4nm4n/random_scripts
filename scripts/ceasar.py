import string
import optparse

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
    
def decrypt(message, shift):    
    message_list = []
    ascii_reference = string.ascii_lowercase
    ascii_list = []
    char_list = []
    cleartext = ""
    
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
        
    length = 26-shift
    end = 52-shift
    
    char_list = char_list[length:end]

    ## loop through characters in example_list, find the index of each letter in 
    ## ascii_list and shift it by 2, then append each character to the answer 
    ## string. To avoid out of range index, make special cases for 'y' and 'z'
    
    
    for i in message_list:
        if i != " ":
            new_index = ascii_list.index(i)
            new_char = char_list[new_index]
            cleartext += new_char
        else:
            new_char = i
            cleartext += new_char
    return cleartext
 
def encrypt(message, shift):    
    message_list = []
    ascii_reference = string.ascii_lowercase
    ascii_list = []
    char_list = []
    ciphertext = ""

    ## split ascii string into searchable list
    for char in message:
        message_list.append(char)
    for char in ascii_reference:
        ascii_list.append(char)

    ## split example string into searchable list. To account for the last x
    ## characters in the alphabet, make the list repeat itself once. where x
    ## is given by the value in "shift"
    for char in ascii_reference:
        char_list.append(char)
    for char in ascii_reference:
        char_list.append(char)
        
    ## cut off the extra duplicates
    length = 26 + shift
    start = shift
    char_list = char_list[start:length]

    ## loop through characters in example_list, find the index of each letter in 
    ## ascii_list and shift it by 2, then append each character to the answer 
    ## string. To avoid out of range index, make special cases for 'y' and 'z'
    for i in message_list:
        if i != " ":
            new_index = ascii_list.index(i)
            new_char = char_list[new_index]
            ciphertext += new_char
        else:
            new_char = i
            ciphertext = ciphertext + new_char
    return ciphertext
    
    
options = get_arguments()
shift = int(options.shift)

if not options.method:
    print(encrypt(options.message, shift))
else:
    print(decrypt(options.message, shift))
