
#read file
def read_file(path, action):
    file = open(path, action)    
    #print(file.read())
    return file

def menu():
    print("\nMemory Book Application\n")
    choice = 1
    while choice != 0:
        choice = input("Digite 1 to english/portuguese or 2 portuguese english? ")
        if choice == "1":
            print("English/Portuguese chosen!")
            print(choice)
            cad_word("en-pt.txt","english")
        if choice == "2":
            print("Portuguese/English chosen!")
            print(choice)
            cad_word("pt-en.txt","portuguese")
        if choice == "0":
            print("Exit!")
            exit()

def cad_word(fileName, language):
    word = input("Digite the "+language+" word: ")
    translation = input("Digite translation: ")
    file = read_file(fileName, "a")
    file.write(word+": "+translation+"\n")
    file.close()

menu()
