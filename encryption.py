# -*- coding: utf-8 -*-
"""
Created on Wed Jul 30 20:26:45 2025

@author: gramk
"""

from datetime import datetime

def encrypt_message(string):
    CRYPTO = []

    for i in string:
        a = ord(i) # string to ascii
        CRYPTO.append(a)

    time_password = datetime.now().strftime("%H%M")
    
    KEY = int(time_password)
    #print()

    Encrpted_Crypto = []
    for i in CRYPTO:
        d = i^KEY 
        Encrpted_Crypto.append(d)

    return Encrpted_Crypto, KEY, CRYPTO


