# -*- coding: utf-8 -*-
"""
Created on Wed Jul 30 20:33:07 2025

@author: gramk
"""


def decrypt_message(Encrpted_Crypto, KEY):
    Decrypted_Crypto = []
    for i in Encrpted_Crypto:
        f = i^KEY
        Decrypted_Crypto.append(f)
    #for i in Decrypted_Crypto:
        #g = chr(i) # ascii to string
        #print(g,end='')
    decrypted_text = ''.join(chr(j) for j in Decrypted_Crypto)
    
    return Decrypted_Crypto,  decrypted_text
    
#print(decrypt_massage([12,13,14], 125))