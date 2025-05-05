import random
print(r''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       ''')
stages = ['''
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
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
low=['head','tail','hand','body','leg','finger']
word=random.choice(low)
c=0
lt=[]
for j in word:
    lt.append("_")
j=len(word)
while(c<=6 and j>0):
    l=input("Guess the word:")
    if l in word:
        lt[word.find(l)]=l
        print(" ".join(lt))
        word=word.replace(l,"_")
        j-=1
    else:
        print(" ".join(lt))
        print(stages[c])
        c+=1
if(j==0):
    print("You Won")
else:
    print("You Lost")
    print(word)


