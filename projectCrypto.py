import re
import projectMath
from math import gcd, sqrt

class HillCipher:
    def setEncryptionMatrix(self, encryptionMatrix):
        det = projectMath.matrixDeterminant(encryptionMatrix, 26)
        if gcd(det, 26) != 1:
            raise Exception("Determinant is not coprime with 26!")
        else:
            self.encryptionMatrix = encryptionMatrix
            self.decryptionMatrix = projectMath.matrixInversion(encryptionMatrix, 26)

    def setEncryptionMatrixWithPassword(self, key):
        encryptionMatrix = keywordToMatrix(key)
        self.setEncryptionMatrix(encryptionMatrix)

    def encrypt(self, message):
        messageMatrix = textToMatrixWithPadding(message, len(self.encryptionMatrix))
        outputMatrix = projectMath.matrixMultiplication(self.encryptionMatrix, messageMatrix, 26)
        outputMessage = matrixToText(outputMatrix)
        return outputMessage

    def decrypt(self, ciphertext):
        ciphertextMatrix = textToMatrixWithPadding(ciphertext, len(self.decryptionMatrix))
        outputMatrix = projectMath.matrixMultiplication(self.decryptionMatrix, ciphertextMatrix, 26)
        outputMessage = matrixToText(outputMatrix)
        return outputMessage

def keywordToMatrix(input):
    border = int(sqrt(len(input))) + 1
    size = 0
    for i in range(1, border + 1):
        if (i * i == len(input)):
            size = i
    if size == 0:   # sprawdzenie, czy dlugosc klucza to kwadrat naturalnej
        raise Exception("string must be a square of an integer!")
    else:
        output = [[0 for row in range(size)] for col in range(size)] # stworzenie pustej macierzy
        it = 0
        for i in range(len(output)):
            for j in range(len(output)):
                output[i][j] = ord(input.upper()[it]) - 65 # zapelnienie macierzy kluczem
                it += 1
        return output

def removeNonAlphabeticalSimbols(input):
    from re import compile
    reg = compile("[^a-zA-Z]")  # regex którego musi odpowiadać tekst
    return reg.sub('', input)   # usunięcie wszystkich znaków, z wyjątkiem odpowiadających reg

def padTextToNumberMultiplication(input, number):
    rem = len(input) % number
    if rem != 0:
        paddingSize = number - rem  # ile znaków brakuje
        padding = ''.join(["X" for i in range(paddingSize)])    # stworzenie paddingu za pomocą listy składanej
        return input + padding
    else:
        return input    # gdy tekst jest wielokrotnością n, brak dopełnienia

def textToUpper(input):
    return input.upper()

def textToMatrixWithPadding(input, ngram):
    temp = removeNonAlphabeticalSimbols(input)  # usuniecie wszystkich niealfabetycznych znakow
    temp = padTextToNumberMultiplication(temp, ngram) # padding tekstu
    output = []
    for i in range(ngram):
        output.append([(ord(temp.upper()[j]) - 65) for j in range(len(temp)) if j % ngram == i])
        # zamiana tekstu na macierz
    return output

def matrixToText(input):
    '''
    Zamiana macierzy na tekst. Z racji, że ciężko jest czytać kolumnami tekst, dużo prościej
    najpierw stransponować macierz i czytać dopiero wtedy wierszami.
    '''
    transInput = projectMath.matrixTransposition(input) # transpozycja macierzy wejsciowej
    output = ""
    for i in range(len(transInput)):
        for j in range(len(transInput[0])):
            output += chr(transInput[i][j] + 65)    # dopisywanie do tekstu wyjsciowego aktualnego znaku
    return output
