# -*- coding: utf-8 -*-
"""
Created on Wed Jul 30 21:01:30 2025

@author: gramk
"""



from encryption import encrypt_message
from decryption import decrypt_message


#string = "Here go" 
string = input(" Enter text : ")
print()


Encrpted_Crypto, KEY, CRYPTO = encrypt_message(string)


print("The massage is : ", CRYPTO)
print("Encrypted form of ASCII : ", Encrpted_Crypto)
print("key is the time:", KEY)
print("^^^ This is just for knowledge & verification, should not visible to user ^^^\n")


for i in range(4,0,-1): # range is used this type for the 76th line.
    
    USER_key = int(input("Enter the key : "))
    print()
    
    if (USER_key == KEY):
        
        Decrypted_Crypto, decrypted_text = decrypt_message(Encrpted_Crypto, USER_key)
        for i in Encrpted_Crypto:
            f = i^KEY
            Decrypted_Crypto.append(f)
        print("Decrypted form of Encrypted  form : ", Decrypted_Crypto)
        print("^^^ This is just for knowledge & verification, should not visible to user ^^^\n")

        print("The Text was :  ",decrypted_text)
        
        break
    else:
        print("Wrong key entered !! , You have last ",i-1," chance left")
