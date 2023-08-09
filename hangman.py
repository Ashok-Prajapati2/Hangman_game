#########################################################
##        File Name: hangman.py                        ##
##        Description:  Hangman project                ##
#########################################################

import random
from word import word_list
import img 

print(img.welcome + img.logo)

stages = img.stages

word_chouse = random.choice(word_list)
print(word_chouse)

ch_list = []
for n in range(len(word_chouse)):
    ch_list += "_"
print(ch_list)    

game_is_end = False

lives = 6

while not game_is_end:
    user_input = (input("ENTER  LETTER : ")).lower()
    # print(user_input)

    for word in range(len(word_chouse)):
        latter = word_chouse[word]
        # print(f"{word} {word_chouse} {latter}")
        
        if latter == user_input:
            ch_list[word] = user_input
         
        else:
            pass
    if latter not in user_input :
        lives -= 1  
        print(f"your {lives} attend remainig") 
        print(stages[-lives-1])  
        if lives == 0:
            game_is_end= True
            print("You lose!")
        
    if not "_" in ch_list:
        game_is_end= True
        print("Game Over!")
        
    
    
    f_word = ""
    for n in ch_list:
         f_word += n
    
    print(f"Your progress {f_word}")     
