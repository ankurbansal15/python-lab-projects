from random import randint
h1 = chr(0x203E)*7
dice = {
    1 : f" _______\n|       |\n|   0   |\n|       |\n {h1}",
    2 : f" _______\n|0      |\n|       |\n|      0|\n {h1}",
    3 : f" _______\n|0      |\n|   0   |\n|      0|\n {h1}",
    4 : f" _______\n|0     0|\n|       |\n|0     0|\n {h1}",
    5 : f" _______\n|0     0|\n|   0   |\n|0     0|\n {h1}",
    6 : f" _______\n|0     0|\n|0     0|\n|0     0|\n {h1}"
}
t = int(input("Enter number of times you want to throw dice:\n"))
pile=[]
for i in range(t):
    pile.append(randint(1,6))
for i in pile:
    print(dice[i])
input("Enter to exit program.")