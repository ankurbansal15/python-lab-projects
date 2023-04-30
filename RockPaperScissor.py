from random import randint
while True:
    lst = ["rock","paper","scissor","rock"]
    user = input("Choose: \n")
    cpu = lst[randint(0,3)]
    if user not in lst:
        print("Invalid Move")
        continue
    print("Computer chooses:",cpu.upper())
    if cpu == user:
        print("DRAW")
    else:
        print("You Loss") if lst[lst.index(user)+1] == cpu else print("You win") 
    if input("play again (y) or exit (n)") == "n": break