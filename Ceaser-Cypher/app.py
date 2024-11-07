alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
def move_in_order(task, move_num, inpt):
    result = ""
    for i in inpt:
        if i in alphabet:
            chosen_char_index = alphabet.index(i) + move_num
            if chosen_char_index >= 26:
                indx = chosen_char_index - 26
            else:
                indx = chosen_char_index
            result += alphabet[indx]
        else:
            result += i
    return result

def enc_dec_rypt(*argv):
    inpt = argv[0]
    task = argv[1]
    move_num = argv[2]    
    result = ""
    if task == "encrypt" and len(argv) > 2:
        result = move_in_order(task, move_num, inpt)
    else:
        result = move_in_order(task, -move_num, inpt)
    print(f"The result is: {result}")

inpt = str(input("Type encrypt for encrypting, decrypt for decrypting: ")).lower()
if inpt == 'encrypt':
    argv = str(input("Please enter the message: "))
    move_num = int(input("Please input number of moving as well: "))
    enc_dec_rypt(argv, inpt, move_num)
elif inpt == 'decrypt':
    argv = str(input("Please enter the code-message: "))
    move_num = int(input("Please input number of moving as well: "))
    enc_dec_rypt(argv, inpt, move_num)
else:
    print('Wrong input')