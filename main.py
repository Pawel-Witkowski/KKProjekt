import projectCrypto
import sys

if __name__ == "__main__":
    print("Greetings. That's example application of HillCipher \t done by Pawel Witkowki")
    text = ""
    if len(sys.argv) != 1:
        pathToFile = sys.argv[1]
        try:
            with open(pathToFile, "r") as file:
                text = file.read()
            print("Application loaded file from parameter as an input text")
        except Exception as e:
            print ("Error " + str(e))
            print("Sorry, you've passed wrong path. You have to enter path file manually on console")

    while text == "":
        pathToFile = input("Please, enter file path.")
        try:
            with open(pathToFile, "r") as file:
                text = file.read()
            print("Application loaded file from parameter as an input text")
            succesfulInput = True
        except Exception as e:
            print ("Error " + str(e))

    hill = projectCrypto.HillCipher()
    succesfulKey = False
    while not succesfulKey:
        try:
            key = input("Please, enter ASCII letters secret key")
            hill.setEncryptionMatrixWithPassword(key)
            succesfulKey = True
        except Exception as e:
            print("Error " + str(e))

    cipher = hill.encrypt(text)
    print (cipher)
    plain = hill.decrypt(cipher)
    print (plain)


    # matrix2 = [
    #     [2, 5, 7],
    #     [6, 3, 4],
    #     [5, -2, -2]
    # ]


