import secrets

sign = ' 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!ąęć:()#$%^&*'

salt = secrets.token_hex(3) # create a salt function later add to encrypted message


letter_index = dict(zip(sign, range(len(sign)))) # create dictionary letter to index
index_letter = dict(zip(range(len(sign)), sign)) # create dictionary index to letter

def encrypt(message, key): # fuction to encrypt
    encrypted = ''
    # split message using lenght of given key
    splitMessageKey = [message[i:i + len(key)] for i in range(0, len(message), len(key))]

    for every_split in splitMessageKey:
        i = 0
        for letter in every_split:
            number = (letter_index[letter] + letter_index[key[i]]) # add letter form message and letter from key
            encrypted += index_letter[number]
            i += 1

    return salt + encrypted

def decrypted(encM, key):
    decrypted = ''

    encM2 = encM[6:] # remove salt form cipher message

    splitEncM = [encM2[i:i + len(key)] for i in range(0, len(encM2), len(key))]

    for each_split in splitEncM:
        i = 0
        for letter in each_split:
            number = (letter_index[letter] - letter_index[key[i]]) #remove letter from key
            decrypted += index_letter[number]
            i += 1

    return decrypted
