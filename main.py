pirmais = int(input("Izvēlies pirmo skaitli: "))
otrais = int(input("Izvēlies otro skaitli: "))
veids = input("Izvēlies veidu (+,-,*,/): ")

#1 +
def plusot(x, y):
    print(x + y)
    return x + y
#2 -

#3 *
def reizot(x, y):
    print(x * y)
    return x * y
#4 /

if veids == "+":
    plusot(pirmais, otrais)

if veids == "*":
    reizot(pirmais, otrais)
