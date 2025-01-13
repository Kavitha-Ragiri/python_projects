import random
import hangman_stages
word_list=["beautiful","handsome","mindblowing","awesome","lovely","super","amazing",
           "gorgeous","fantastic",""]
lives=6
choosen_word=random.choice(word_list)
print(choosen_word)

display=[]

for i in range(len(choosen_word)):
    display+='_'
print(display)

game_over=False
while not game_over:

    guess_letter=input("Guess a letter")

    for position in range(len(choosen_word)):
        letter=choosen_word[position]
        if letter==guess_letter:
            display[position]=guess_letter
    print(display)
            
    if guess_letter not in choosen_word:
        lives-=1
        if lives==0:
            game_over=True
            print("You Lose!!")
            

    if '_' not in display:
        game_over=True
        print("You Win!!")
    print(hangman_stages.stages[lives])
