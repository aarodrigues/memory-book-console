import random

list = []

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
    word = ""
    while word != "0":
        word = input("Digite the "+language+" word: ")
        if not exist(fileName,word):
            if(word != "0"):
                translation = input("Digite translation: ")
                file = read_file(fileName, "a")
                file.write(word+" : "+translation+"\n")
                file.close()
        else:
            print("Word already exist! Please try again")

def exist(fileName,word):
    with open(fileName) as fp:
        line = fp.readline()
        while line:
            if(word == line.strip().split(" ",1)[0]):
                return True
            line = fp.readline()
        return False

def get_list(fileName):

    with open(fileName) as fp:
        line = fp.readline()
        while line:
            list.append(line.strip())
            line = fp.readline()
        print(len(list))

def get_random_element():
    print(random.choice(list))



#menu()

#r = exist("en-pt.txt", "red:")
#print(r)

get_list("en-pt.txt")
get_random_element()