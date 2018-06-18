import projectCrypto
from re import sub
import os
if __name__ == "__main__":
    print("Greetings. That's example application of HillCipher \t done by Pawel Witkowki")
    text = ""
    key = ""
    answer = "1"
    fileMode = False
    hill = projectCrypto.HillCipher()
    while answer != "\n":
        print("What would you like to do? \n 1. load text \n 2. encrypt text \n 3. decrypt text")
        answer = input()
        if int(answer) == 1:
            encryptFile = input("Please, enter filepath. If there is no such file, I will load it as a raw text")
            try:
                with open(encryptFile, "r") as file:
                    text = file.read()
                fileMode = True
            except:
                print ("Wrong path! I loaded your string as a raw text!")
                text = encryptFile
                fileMode = False
        else:
            succesfulKey = False
            while not succesfulKey:
                key = input("Please, insert your keyword. Key has to be square value of int, and his matrix form must be reversible mod26")
                try:
                    hill.setEncryptionMatrixWithPassword(key)
                    succesfulKey = True
                except Exception as e:
                    print("Error " + str(e))
            if int(answer) == 2:
                output = hill.encrypt(text)
                if fileMode:
                    with open(os.path.abspath(encryptFile) + ".enc", "w") as file:
                        file.write(output)
                else:
                    print ("Your encrypted message is \n " + output)
            elif int(answer) == 3:
                output = hill.decrypt(text)
                if fileMode:
                    with open(os.path.abspath(encryptFile).replace(".enc", ".dec"), "w") as file:
                        file.write(output)
                else:
                    print ("Your decrypted message is \n " + output)
            else:
                print("Invalid mode, please try again")

## cfhgdefyy
    # matrix2 = [
    #     [2, 5, 7],
    #     [6, 3, 4],
    #     [5, -2, -2]
    # ]


