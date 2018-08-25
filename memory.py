import random

list = []

#read file
def read_file(path, action):
    file = open(path, action)    
    #print(file.read())
    return file

#application menu
def menu():
    print("\nMemory Book Application\n")
    choice = 1
    while choice != 0:
        choice = input("Digite 1 to register a new word or Digite 2 to traning with registered words: ")
        if choice == "1":
            menu_cad()
        if choice == "2":
            menu_training()
        if choice == "0":
            print("Exit!")
            exit()

#register menu
def menu_cad():
    print("\nWord Register\n")
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
            break

#training menu
def menu_training():
    print("\nBegin training!\n")
    gameType = input("Do you want to practice portuguese/english (Digite 1) or english portuguese (Digite 2): ")
    if gameType == "1":
        get_list("pt-en.txt")
    if gameType == "2":
        get_list("en-pt.txt")
    userInput = 1
    while userInput != 0:
        line = get_random_element()
        word = line.split(" ",1)[0]
        userInput = input(word+ " ")
        answer = line.split(" ",1)[-1].strip()
        if userInput.strip() == answer:
            print("Right, Congradulations!")
        elif userInput.strip() == " ":
            break
        else:
            print("Wrong, try again")
                
#register word
def cad_word(fileName, language):
    word = ""
    while word != "0":
        word = input("Digite the "+language+" word: ")
        if not exist(fileName,word):
            if(word != "0"):
                translation = input("Digite translation: ")
                file = read_file(fileName, "a")
                file.write(word+": "+translation+"\n")
                file.close()
        else:
            print("Word already exist! Please try again")

#find ocurrence
def exist(fileName,word):
    with open(fileName) as fp:
        line = fp.readline()
        while line:
            if(word == line.strip().split(" ",1)[0]):
                return True
            line = fp.readline()
        return False

#fill list from file
def get_list(fileName):

    with open(fileName) as fp:
        line = fp.readline()
        while line:
            list.append(line.strip())
            line = fp.readline()

#get random line from list
def get_random_element():
    return random.choice(list)


#entry point
menu()