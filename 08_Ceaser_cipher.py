
def encrypt(message, shift):
    message = [ord(c) for c in message]
#    print(message)
    for i in range(len(message)):
        if message[i] >= 65 and message[i]<= 90:
            if message[i]+shift > 90:
                message[i] = ((message[i]+shift)%90)+64
            else:
                message[i] = message[i]+shift
        elif message[i] >=97 and message[i] <= 122:
            if message[i]+shift > 122:
                message[i] = ((message[i]+shift)%122)+96
            else:
                message[i] = message[i]+shift
#    print(message)
    message = [chr(n) for n in message]
    message = ''.join(message)
    return message


def decrypt(message, shift):
    message = [ord(c) for c in message]
    for i in range(len(message)):
        if message[i] >= 65 and message[i]<= 90:
            if message[i]-shift < 65:
                message[i] = ((message[i]-shift)+26)
            else:
                message[i] = message[i]-shift
        elif message[i] >=97 and message[i] <= 122:
            if message[i]-shift < 97:
                message[i] = (message[i]-shift)+26
            else:
                message[i] = message[i]-shift
    message = [chr(c) for c in message]
    message = ''.join(message)
    return message

def cipher(message, shift, direction):
    if shift > 26:
        shift = shift%26
    if direction == 'encode':
        print(encrypt(message, shift))
    elif direction=='decode':
        print(decrypt(message, shift))
    else:
        print(f'Invalid Arguments : {direction}')



while 1:
    method = str(input('Type \'encode\' to encrypt, type \'decode\' to decrypt:'))
    message = str(input('Enter your message:'))
    shift = 0
    shift = int(input('Enter the shift number:'))
    cipher(message, shift, method)
    cont = str(input('Type \'yes\' to continue. Otherwise type \'no\':'))
    if cont == 'no':
        print('Goodbye.')
        break
