import os
import random
import hashlib


banner1="""
                                            ███████╗██╗███╗   ███╗██████╗ ██╗     ███████╗   
                                            ██╔════╝██║████╗ ████║██╔══██╗██║     ██╔════╝    
                                            ███████╗██║██╔████╔██║██████╔╝██║     █████╗      
                                            ╚════██║██║██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝     
                                            ███████║██║██║ ╚═╝ ██║██║     ███████╗███████╗    
                                            ╚══════╝╚═╝╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝"""
banner2="                                                    |__ by CHAHAT Abdennour _|"
banner3="""                                                                                                                                                    
                     ██████╗██████╗ ██╗   ██╗██████╗ ████████╗ ██████╗  ██████╗ ██████╗  █████╗ ██████╗ ██╗  ██╗██╗   ██╗
                    ██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██╔═══██╗██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██║  ██║╚██╗ ██╔╝
                    ██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ██║   ██║██║  ███╗██████╔╝███████║██████╔╝███████║ ╚████╔╝ 
                    ██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██║   ██║██║   ██║██╔══██╗██╔══██║██╔═══╝ ██╔══██║  ╚██╔╝  
                    ╚██████╗██║  ██║   ██║   ██║        ██║   ╚██████╔╝╚██████╔╝██║  ██║██║  ██║██║     ██║  ██║   ██║   
                     ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝   ╚═╝   
"""

def clearTerminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# colors
def print_red(text):
    print(f"\033[91m{text}\033[0m")
def print_green(text):
    print(f"\033[92m{text}\033[0m")
def print_yellow(text):
    print(f"\033[93m{text}\033[0m")
def print_blue(text):
    print(f"\033[94m{text}\033[0m")
def print_magenta(text):
    print(f"\033[95m{text}\033[0m")
def print_cyan(text):
    print(f"\033[96m{text}\033[0m")

# caesar cipher encryption and decryption functions
def stayInASCIIRange(num):
    if num>122:
        num%=122
        num+=96
    return num
def caesarEncryption(string,shift):
    result=""
    for ch in string:
        if ch.isalpha():
            result+=chr(stayInASCIIRange(ord(ch)+shift))
        else:
            result+=ch
    return result

def caesarDecryption(string,shift):
    return caesarEncryption(string,26-shift)

def isInteger(inputValue):
    try:
        int(inputValue)
        return True
    except ValueError:
        return False
# substitution cipher 
def keyGenerator():
    result=""
    alphabets = list("abcdefghijklmnopqrstuvwxyz")
    for i in range(0,26):
        num=random.randint(0,25-i)
        result+=alphabets[num]
        alphabets.pop(num)
    return result

def getIndexCharacter(ch,b_list):
    for i in range(0,26):
        if ch==b_list[i]:
            return i

def substEncryption(string,key):
    result=""
    i=0
    for ch in string:
        if ch.isalpha():
            if ch.islower():
                result+=key[getIndexCharacter(ch,list("abcdefghijklmnopqrstuvwxyz"))]
            else:
                result+=key[getIndexCharacter(ch.lower(),list("abcdefghijklmnopqrstuvwxyz"))].upper()
        else:
            result+=ch
    return result

def substDecryption(string,key):
    result=""
    alphabets=list("abcdefghijklmnopqrstuvwxyz")
    for ch in string:
        if ch.isalpha():
            if ch.islower():
                result+= alphabets[getIndexCharacter(ch,key)]
            else:
                result += alphabets[getIndexCharacter(ch.lower(), key)].upper()
        else:
            result += ch
    return result

#verify string
def verify(string):
    vString="abcdefghijklmnopqrstuvwxyz"
    if len(vString)!=26:
        return False
    return set(string)==set(vString)


# hashing algorithms
hashFunctions = {
    'md5': hashlib.md5,
    'sha3_512': hashlib.sha3_512,
    'blake2b': hashlib.blake2b,
    'sha3_224': hashlib.sha3_224,
    'sha3_384': hashlib.sha3_384,
    'sha1': hashlib.sha1,
    'sha224': hashlib.sha224,
    'blake2s': hashlib.blake2s,
    'sha3_256': hashlib.sha3_256,
    'shake_256': hashlib.shake_256,
    'shake_128': hashlib.shake_128,
    'sha512': hashlib.sha512,
    'sha256': hashlib.sha256,
    'sha384': hashlib.sha384,
}
hashFunctionKeys = list(hashFunctions.keys())

# validation numeric input function
def validateNumericInput(minOption,maxOption,color=4):
    while True:
            inputValue = input(f"\033[9{color}m>> \033[0m")
            if isInteger(inputValue):
                inputValue = int(inputValue)
                if minOption <= inputValue <= maxOption:
                    return inputValue
                else:
                    print_red(f"enter a number between [{minOption} - {maxOption}] !!\n")
            else:
                print_red(f"enter a number between [{minOption} - {maxOption}] !!\n")
            
def validateStringInput():
    while True:
        message=str(input(f"\033[94m>> \033[0m")).strip()
        if message == "":
            print(f"\033[91m !!Enter a string  !! \033[0m\n")
        else : 
            return message

# main
def main():
    choice = None
    clearTerminal()
    print_red("\t\t\t\t\t     Welcome to the Hashing and Encryption Program")
    print_blue(banner1)
    print_red(banner2)
    print_blue(banner3)
    while(choice!=0):
        print_blue("\n\n\t\tMain menu")
        print_blue("\t[1]. Caesar cipher encryption")
        print_blue("\t[2]. Substitution cipher")
        print_blue("\t[3]. Hashing algorithms")
        print_red("\t[0]. Exit") 
        choice=validateNumericInput(0,3)
        match choice:
            case 1:
                print_blue("   \n\t[1] Caesar cipher encryption")
                Description="""\tDescription : It is a type of substitution cipher where each letter is replaced by 
                       the letter located a certain number of positions down or up the alphabet. """
                print_cyan(Description)
                while(choice!=0):
                    print_magenta("\t[1]. Encrypt")
                    print_magenta("\t[2]. Decrypt")
                    print_red("\t[0]. Go Back\n")
                    choice = validateNumericInput(0,2,5)
                    match choice:
                        case 1:
                            print_blue("Enter the message to be encrypted:")
                            message=validateStringInput()
                            print_blue("Enter the shift value:")
                            shift=validateNumericInput(1,25)
                            encryptedText=caesarEncryption(message,shift)
                            print(f"   Encrypted message :\t\033[92m{encryptedText} \033[0m\n\n")
                            
                        case 2:
                            print_blue("Enter the message to be decrypted:")
                            message=validateStringInput()
                            print_blue("Enter the shift value:")
                            print_red("REMARQUE: if you don't know the shift type enter 0")
                            shift=validateNumericInput(0,25)
                            if(shift == 0):
                                for i in range(1,26):
                                    decryptedText=caesarDecryption(message,i)
                                    print(f"   Decrypted message with shift {i} :\t\033[92m{decryptedText} \033[0m\n")
                            else:
                                decryptedText=caesarDecryption(message,shift)
                                print(f"   Decrypted message :\t\033[92m{decryptedText} \033[0m\n\n")
                        case 0:
                            break
                        case _:
                            print_red("Invalid choice")
                choice=1 
            case 2:
                print_blue("\n\t[2]Substitution cipher")
                Description="""\tDescription : alphabets to encrypt the message, often using a keyword to determine the shift
                            at each position.\n"""
                print_cyan(Description)  
                choice=1
                while(choice!=4):
                    print_magenta("\t[1]. Generate a key\n\t[2]. Encrypt\n\t[3]. Decrypt")
                    print_red("\t[0]. Go Back\n")
                    choice=validateNumericInput(0,3,5)
                    match choice:
                        case 1:
                            key=keyGenerator()
                            print(f"   \tKEY : \033[92m{key} \033[0m")
                            print_red("!! REMARQUE: you should copy and save it for encryption and decryption usage !!\n")
                        case 2:
                            print_blue("Enter the message to be encrypted: ")
                            message=validateStringInput()
                            print_blue("Enter the key value that you generated : ")
                            key=validateStringInput()
                            if verify(key):
                                encryptedText=substEncryption(message,key)
                                print(f"   Encrypted message :\t\033[92m{encryptedText} \033[0m\n\n")
                            else:
                                choice=1
                                print_red("\tInvalid key. Select option [1] to generate a key")
                        case 3:
                            print_blue("Enter the message to be decrypted:")
                            message=validateStringInput()
                            print_blue("Enter the key value:")
                            key=validateStringInput()
                            if verify(key):
                                decryptedText=substDecryption(message,key)
                                print(f"   Decrypted message :\t\033[92m{decryptedText} \033[0m\n\n")
                            else:
                                choice=1
                                print_red("Invalid key")
                                print_red("select 1 option to generate a key")
                        case 0:
                            break
                        case _:
                            print_red("Invalid choice")
                choice=2
            case 3:
                choice=1
                while choice!=0 and choice !=2 :
                    print_blue("\n\t[3] Hashing algorithms")
                    print_magenta("\tAvailable hash types : ")
                    i=0
                    for type in hashFunctionKeys:
                        i+=1
                        print_magenta(f"\t\t[{i}] - {type}")
                    print_blue("Select a hash type by enter his number : ")
                    typeSelected=validateNumericInput(1,14) - 1
                    print_blue("Enter a string to hash : ")
                    inputText=validateStringInput().encode()
                    hashObject = hashFunctions[hashFunctionKeys[typeSelected]](inputText)
                    hashResult = hashObject.hexdigest()
                    print(f"The \033[92m{hashFunctionKeys[typeSelected]}\033[0m hash of the input data is : \033[92m{hashResult}\033[0m")
                    print_magenta("Select an option : ")
                    print_magenta("\t[1] Try another hash typ")
                    print_magenta("\t[2] Back to main menu")
                    choice=validateNumericInput(1,2,5)
            case 0:
                print_red("\t\t\t\t\t\t<<Thank you for using this program (: >>")
            case _:
                print_red("Invalid choice")

if __name__ == "__main__":
    main()