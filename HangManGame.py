import random
words = ["update","battery","low","population","character","cultural",
         "flash","at","admire","crack","code","amputate","spirit","urine",
         "me","fairy","mystery","stir","visible","remember","computing","by"
         ,"boy","market","height","undertake","cigarette","issue","ritual","pottery"
         ,"cold","reform","education","hierarchy","abbey","science","vein","anger"
         ,"abundant","hospital","fountain","crash","lamb","hardship","lease","shake"
         ,"soar","harvest","abstract","obese"]

word = random.choice(words)
temp = list(word)
random.shuffle(temp)
print("Missed Letters:",end='')
for i in temp:
    print(i + " ",end='')
print()
missted_word = word
miss_list = []
for i in range(len(word)):
    if((i+2) %2 == 0):
        missted_word = missted_word.replace(word[i],'_')
        miss_list.append(word[i])
print(missted_word)
for i in range(1,11):

    user_input = input("Enter your letter:")
    if(user_input in miss_list):
        miss_list.remove(user_input)
        missted_word = word
        for i in miss_list:
            missted_word = missted_word.replace(i,"_")
        print(missted_word)
        print("Congrulations, Your Letter is Matched")
    else:
        print("Sorry, Your Letter is wrong, Chances Left:", 10-i)
if(missted_word == word):
    print("You Won the Game")
else:
    print("You Loose the Game")
