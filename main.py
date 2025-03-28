pirmais = int(input("Izvēlies pirmo skaitli: "))
otrais = int(input("Izvēlies otro skaitli: "))
veids = input("Izvēlies veidu (+,-,*,/): ")

#1 +
def plusot(x, y):
    print(x + y)
    return x + y
#2 -
def minusot(x, y):
    print(x - y)
    return x - y
#3 *

#4 /

if veids == "+":
    plusot(pirmais, otrais)
elif veids == "-":
    minusot(pirmais, otrais)