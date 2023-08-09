#########################################################
##        File Name: hangman.py                        ##
##        Description:  Hangman project                ##
#########################################################

import random
import word
import img 

print(img.welcome + img.logo)
hung_man = [1,2,3,4,5,6]

word_list = word.word_list
stages = img.stages
print(stages)