
### HANGMAN ####

H1 = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

print('''
welcome to the  game of  HANGMAN
''')
name=input("please enter your name :")
print("hello",name,"play the game:")
num=("holiday")
number=("_")
while True:
    turn=7
    a=0
    while turn>0:
        b=0
        for i in num:
            if i in number:
                print(i)
            else:
                print("_")
                b+=1
        if b==0:
            print("you won")
            break
        guess=input("choose a character")
        number+=guess
        if guess not in num:
            print(H1[a])
            turn-=1
            a+=1
            print("you have",turn,"more chance")
            if turn==0:
                print("you are lose")
    print("do you want to playaaa: y/n ")
    play=input()
    if play =="y":
        print("thank you")
    else:
        print("good bye")
        break                  
