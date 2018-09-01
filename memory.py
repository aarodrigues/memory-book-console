import random

list = []
enpt_txt = "en-pt.txt"
pten_txt = "pt-en.txt"
hits = mistakes = 0

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
        choice = input("Digite 1 to register a new word, Digite 2 to traning with registered words or Digite 3 to list saved words: ")
        if choice == "1":
            menu_cad()
        if choice == "2":
            menu_training()
        if choice == "3":
            list_words()
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
        if line != "":
            word = line.split(" ",1)[0]
            print("\nHits: "+str(hits)+" Mistakes: "+str(mistakes)+"\n")
            userInput = input(word+ " ")
            answer = line.split(" ",1)[-1].strip()
            if userInput.strip() == answer:
                point_count(1)
                print("Right, Congradulations!")
            elif userInput.strip() == "0":
                break
            else:
                point_count(-1)
                print("Wrong, try again")
        else:
            break
                
#register word
def cad_word(fileName, language):
    print("Function cad_word need to be implemented")

#find ocurrence
def exist(fileName,word):
    print("Function exist need to be implemented")

#fill list from file
def get_list(fileName):
    print("Function get_list need to be implemented")

#get random line from list
def get_random_element():
    if len(list) > 0:
        return random.choice(list)
    else:
        return ""

def list_words():
    print("Function list_words need to be implemented")

def point_count(num):
    print("Function point_count need to be implemented")



#entry point
menu()