# Message-encrypt-decrypt-using-TIME_KEY
Message encryptor decryptor using TIME_KEY(new type key)

# python app.py or run app.py

In this full folder you get 3 files :->
1)encrypt.py: In the file you get the logic of encrypting your massage(# string) by 
              i. converting the message's each element in ascii 
              ii. XOR the ascii value list with KEY
              iii. saved in a list (# encrypted_crypto)
              
2) decrypt.py: In the file the encryption processes are reversely done to get the exact message, but here the KEY is vrified if it matches or not
                The KEY is here your system's real time. e.g: if the time is 07:12 then the KEY : 0712 or 712
                
3) ap.py: In this file you get the whole working interface,
         you just need to run only this file ,  the all files are connected by import command 
         Here you enter your text ,
         & then you you need to enter KEY,
         you just have 4 attampt ( line 28 #for i in range(4,0,-1): ) .

   <img width="481" height="780" alt="image" src="https://github.com/user-attachments/assets/67a9500c-2cb7-47e4-a057-07d52c1f69e5" />
