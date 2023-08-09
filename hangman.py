#########################################################
##        File Name: hangman.py                        ##
##        Description:  Hangman project                ##
#########################################################

import random
from word import word_list
import img 

print(img.welcome + img.logo)
print("\n your total attend six")
stages = img.stages

word_choose = random.choice(word_list)
# print(word_choose)

ch_list = []
for n in range(len(word_choose)):
    ch_list += "_"
# print(ch_list)    

game_is_end = False

lives = 6

while not game_is_end:
    user_input = (input("\n ENTER  LETTER : ")).lower()
    # print(user_input)
    
    if user_input in word_choose:
        
        for word in range(len(word_choose)):
        # print(f"{word} {word_chouse} {latter}")
            if word_choose[word] == user_input:
               ch_list[word] = user_input
        
    else:
        lives -= 1  
        print(f"your {lives} attend remainig") 
        print(stages[-lives-1]) 
        if lives == 0:
            game_is_end= True
            print(f"You lose! \n Right word is : {word_choose}")
        
    if not "_" in ch_list:
        game_is_end= True
        print(" You win ")
        print("Game Over!")
        
    
    
  
    print(f"Your progress: {' '.join(ch_list)}")
        

# This a another way (only use for devlper)

# while not game_is_end:

#         user_input = (input("ENTER  LETTER : ")).lower()
#         # print(user_input)
    
#         for word in range(len(word_chouse)):
#             latter = word_chouse[word]
#             # print(f"{word} {word_chouse} {latter}")
            
#             if latter == user_input:
#                 ch_list[word] = user_input
             
#             else:
#                 pass
#         if user_input not in word_chouse :
#             lives -= 1  
#             print(f"your {lives} attend remainig") 
#             print(stages[-lives-1])  
#             if lives == 0:
#                 game_is_end= True
#                 print("You lose!")
            
#         if not "_" in ch_list:
#             game_is_end= True
#             print("Game Over!")
            
        
        
#         f_word = ""
#         for n in ch_list:
#              f_word += n
        
#         print(f"Your progress {f_word}") 