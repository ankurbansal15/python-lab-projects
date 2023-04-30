from random import choices,sample
t = input("Enter 'Y' to generate password\n")
if t.lower() == "y":
    alphaU = list(range(65,91))
    alphaL = list(range(97,123))
    num = list(range(48,58))
    sym = list(range(33,48))+[64]
    passwd = list(map(chr,(choices(alphaU,k=3)+choices(alphaL,k=3)+choices(num,k=3)+choices(sym,k=3))))
    print("".join(sample(passwd,k=12)))
input("Enter to exit program.")