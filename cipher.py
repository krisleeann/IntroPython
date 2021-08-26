import sys

def pathway():
    
    if len(sys.argv) < 3:
        print("USAGE: python3 cipher.py your_keyword -d(optional) input_file.txt output_file.txt")
    else:
        # Assign keyword and path from command line args; spec: only work on uppercase alpha chars 
        keyword = sys.argv[1].capitalize()
        
        if sys.argv[2] == '-d':
            # For decryption, read encrypt.txt 
            with open(sys.argv[3], 'r') as file:
                orig_text = file.read().upper()
            print(encrypt(keyword, orig_text))
        else: 
            # For encryption, read input.txt
            with open(sys.argv[2], 'r') as file: 
                orig_text = file.read().upper()
            print(decrypt(keyword, orig_text))

def encrypt(keyword, orig_text):
    # encrypt contents of input.txt and place result in encrypt.txt
    encrypted = []
    
    for i in range(len(orig_text)): 
        # Bug: IndexError: string index out of range
        # encode = (((ord(keyword[i]) - ord(orig_text[i]) % 26) / 26) + ord('A'))
        # encrypted.append(encode)
        pass
    
    # Bug: IndexError: list index out of range
    # with open(sys.argv[4], 'w') as encrypting:
    #     encrypting.write(encrypted) 

    return encrypted

def decrypt(keyword, orig_text):
    # decrypt contents of encrypt.txt and place result in output.txt
    decrypted = []

    for i in range(len(orig_text)):
        # Bug: IndexError: string index out of range
        # encode = (((ord(keyword[i]) - ord(orig_text[i]) % 26) / 26) + ord('A'))
        # decrypted.append(encode)
        pass
    
    # Bug: IndexError: list index out of range
    # with open(sys.argv[5], 'w') as output:
    #     output.write(decrypted)
    
def main():
    pathway()

main()
