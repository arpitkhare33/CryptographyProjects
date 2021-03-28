#Cryptography using Vigenere cipher algorithm
import getpass
plainText =input("Enter the statement which you want to encrypt...")
key=getpass.getpass("Enter the key using which you want to do the encryption")
m=len(key)
plainText=plainText.replace(" ","")
plainText=plainText.lower()


textList=[]
i=0
while i<len(plainText):
    textList.append(plainText[i:m])
    i=i+len(key)
    m=m+len(key)

print(textList)
def convert(s):
  
    # initialization of string to ""
    new = ""
  
    # traverse in the string 
    for x in s:
        new += x 
  
    # return string 
    return new
         

def encrypt(textList,key):
    codeList=[]
    for item in textList:
        codeWord=[]
        for i in range(0,len(item)):
            code=(ord(item[i])-97+ord(key[i])-65)%26
            codeWord.append(chr(code+65))
        # print(codeWord)
        str=convert(codeWord)
        codeList.append(str)
    return codeList


def decrypt(textList):
    key=getpass.getpass("Enter the key for decryption")
    codeList=[]
    for item in textList:
        codeWord=[]
        for i in range(0,len(item)):
            code=(ord(item[i])-65-ord(key[i])-65)%26
            codeWord.append(chr(code+97))
        # print(codeWord)
        str=convert(codeWord)
        codeList.append(str)
    codeList=convert(codeList)
    return codeList
cipherText=encrypt(textList,key)
print(cipherText)
print(decrypt(cipherText))