import os
import argparse
import hashlib
import time

# Banner
banner1 = """	
                                        ██   ██  █████  ███████ ██   ██
                                        ██   ██ ██   ██ ██      ██   ██
                                        ███████ ███████ ███████ ███████
                                        ██   ██ ██   ██      ██ ██   ██
                                        ██   ██ ██   ██ ███████ ██   ██"""
banner2="""                                          |___ by CHAHAT Abdennour ___|"""
banner3="""
                            ██████  ██████  ███████  █████  ██   ██ ███████ ██████ 
                            ██   ██ ██   ██ ██      ██   ██ ██  ██  ██      ██   ██
                            ██████  ██████  █████   ███████ █████   █████   ██████
                            ██   ██ ██   ██ ██      ██   ██ ██  ██  ██      ██   ██
                            ██████  ██   ██ ███████ ██   ██ ██   ██ ███████ ██   ██
"""
banner4="""             ____________________________________________________________________________________
            |  USAGE:                                                                            |
            |           python3 password_cracker.py \"hashValue\" -w path/to/passwords/list.txt    |
            |____________________________________________________________________________________|      """

def clearTerminal():
    if os.name == 'nt':
        os.system('cls') 
    else:
        os.system('clear') 


def printBanner():
    clearTerminal()
    print_blue(banner1)
    print_red(banner2)
    print_blue(banner3)
    print_red(banner4)

# Colors
def print_red(text):
    print(f"\033[91m{text}\033[0m")
def print_green(text):
    print(f"\t\t\033[92m{text}\033[0m")
def print_yellow(text):
    print(f"\033[93m{text}\033[0m")
def print_blue(text):
    print(f"\033[94m{text}\033[0m")
def print_magenta(text):
    print(f"\033[95m{text}\033[0m")
def print_cyan(text):
    print(f"\033[96m{text}\033[0m")

# Function to return possible hash types of the hash value
def getHashType(hashValue):
    hashLength=len(hashValue)
    hashTypes={
        32: 'md5',
        40: 'sha1',
        56: ['sha224', 'sha3_224'],
        64: ['sha256', 'sha3_256', 'blake2s'],
        96: ['sha384', 'sha3_384'],
        128: ['sha512', 'sha3_512', 'blake2b']
    }
    possibleHashType=hashTypes.get(hashLength)
    return possibleHashType

# Function to compare the hash value with possible passwords
def passwordCracker(hashValue, passwords, type):
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
        'sha512': hashlib.sha512,
        'sha256': hashlib.sha256,
        'sha384': hashlib.sha384,
    }
    #Compare password with each line in passwords file
    hashFunction = hashFunctions.get(type)
    for password in passwords:
        passwordTemp=hashFunction(password.encode()).hexdigest()
        if hashValue==passwordTemp:
            return password
    return None

def main():
    printBanner()
    parser = argparse.ArgumentParser(description='Process some arguments.')
    parser.add_argument('hash', type=str, help='Hash value')
    parser.add_argument('-w', '--wordlist', type=str, required=True, help='Path to the passwords file')
    args = parser.parse_args()
    
    # Get hash type
    resultType = getHashType(args.hash)
    if resultType == None:
        print_red("\n\n\t !! Unknown hash type !!")
        exit(0)
    hashType = []
    if isinstance(resultType, str):
        hashType.append(resultType)
    elif isinstance(resultType, list):
        hashType.extend(resultType)

    # Open passwords file
    content = []
    try:
        with open(args.wordlist, 'rb') as file:
            for line in file:
                content.append(line.decode('utf-8', errors='ignore').strip())
    except FileNotFoundError:
        print_red(f'The file {args.wordlist} does not exist.')
        return
    except Exception as e:
        print_red(f'An error occurred: {e}')
        return

    print_magenta("Possible types of this hash are : ")
    for ht in hashType:
        print_magenta(f"\t + : {ht}")
    
    print_blue("\n[*] Crack operation start ...")
    for type in hashType:
        print_blue(f"    + : {type}")
        startTime = time.time()
        result = passwordCracker(args.hash, content, type)
        endTime = time.time()
        duration = endTime - startTime
        if result is None:
            print_red("\t  Password not found\n")
            print_blue(f"[*] Crack operation completed in {duration:.2f} seconds")
        else:
            print(f"\t  Password found :\t\033[92m{result} \033[0m\n\n")
            print_blue(f"[*] Crack operation completed in {duration:.2f} seconds")
            break 
        
if __name__ == "__main__":
    main()
