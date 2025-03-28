pirmais = int(input("Izvēlies pirmo skaitli: "))
otrais = int(input("Izvēlies otro skaitli: "))
veids = input("Izvēlies veidu (+,-,*,/): ")

#1 +
def plusot(x, y):
    print(x + y)
    return x + y
#2 -
if veids == "-":
    print(pirmais - otrais)
#3 *

#4 /

if veids == "+":
    plusot(pirmais, otrais)
