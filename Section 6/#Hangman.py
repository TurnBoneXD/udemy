import random
import Hangman_words
import Hangman_art
print(Hangman_art.logo)
print("100+ word hangman!!!")
print("โปรแกรมนี้พัฒนาโดย นาย ภูมิภัทร จิตรีโภชน์")
print("This program is created by Phumipat Jitreephot\n\n")


random_word = random.choice(Hangman_words.word_list)
stage_level = 7
chance = 7
change_word = []
for change in random_word:
    change_word.append("_")
print("-----------------------------------------------------------------")
print(change_word)
game_end = False
while not game_end:
  print(Hangman_art.stages[stage_level])
  guess_letter = input("Guess a letter : ").lower()
  for index in range(len(random_word)):
    if guess_letter == random_word[index]:
      change_word[index] = guess_letter
  print("-----------------------------------------------------------------")
  print(change_word)
  
         
  if guess_letter not in random_word:
    chance -= 1
    stage_level -=1
    if chance == 0:
      print("-----------------------------------------------------------------")
      print(Hangman_art.stages[stage_level])
      print("The word is",random_word)
      print("You Lose!!!")
      game_end = True
    
  if "_" not in change_word:
    print("You Win!!!")
    game_end = True

  



