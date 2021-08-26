def song():
    rhymes = ["on my drum", "on my shoe", "on my tree", "on my door", "on my hive", "on my sticks", "up in heaven", "on my gate", "on my spine", "on my hen"]

    for i in range (len(rhymes)):
        print("This old man, he played %i" % i)
        print("He played knick knack on my %s" % rhymes[i])
        print("With a nick-nack paddy-whack, give the dog a bone,")
        print("This old man came running home.\n")

def main():
    song()

main()