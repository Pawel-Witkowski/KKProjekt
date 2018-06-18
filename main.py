import projectCrypto
from re import sub, compile
import os
if __name__ == "__main__":
    print("Greetings. That's example application of HillCipher \t done by Pawel Witkowki")
    text = ""
    key = ""
    answer = "1"
    fileMode = False
    hill = projectCrypto.HillCipher()
    while answer != "":
        answer = input("What would you like to do? \n 1. load text \n 2. encrypt text \n 3. decrypt text\n")
        if answer == "1":
            encryptFile = input("Please, enter filepath. If there is no such file, I will load it as a raw text\n")
            try:
                with open(encryptFile, "r") as file:
                    text = file.read()
                fileMode = True
            except:
                print ("Wrong path! I loaded your string as a raw text!")
                text = encryptFile
                fileMode = False
        else:
            if text != "":
                succesfulKey = False
                key = ""
                while not succesfulKey and key == "":
                    key = input("Please, insert your keyword. Key has to be square value of int, and his matrix form must be reversible mod26\n")
                    try:
                        hill.setEncryptionMatrixWithPassword(key)
                        succesfulKey = True
                    except Exception as e:
                        print("Error " + str(e))
                if answer == "2":
                    output = hill.encrypt(text)
                    if fileMode:
                        with open(os.path.abspath(encryptFile) + ".enc", "w") as file:
                            file.write(output)
                    else:
                        print ("Your encrypted message is \n " + output)
                elif answer == "3":
                    output = hill.decrypt(text)
                    if fileMode:
                        filePath, suffix = os.path.splitext(os.path.abspath(encryptFile))
                        if suffix == ".enc":
                            with open(filePath + ".dec", "w") as file:
                                file.write(output)
                        else:
                            with open(os.path.abspath(encryptFile) + ".dec", "w") as file:
                                file.write(output)
                    else:
                        print ("Your decrypted message is \n " + output)
                else:
                    print("Invalid mode, please try again")
            else:
                print ("Please, load text to bufor first")

    # cfhgdefyy
    # matrix2 = [
    #     [2, 5, 7],
    #     [6, 3, 4],
    #     [5, -2, -2]
    # ]


