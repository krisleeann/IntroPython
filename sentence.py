def punct(message):
    if message.endswith('!'):
        print("Exclamatory")
    elif message.endswith('?'):
        print("Interrogative")
    elif message.endswith('.'):
        print("Declarative")
    else:
        print("Bad ending")
    
def main():
    x = (input("Enter a sentence: "))
    punct(x)
    
main()