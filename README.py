# small-program

def insertEtoile(arg):
    for i in range(len(arg)):
        print(arg[i], end="")
        if i != len(arg) - 1:
            print("*", end="")
insertEtoile("Python")

elt = 1
for i in range(1, 8):
    print("*" * elt)
    elt += 1

t3 = []
t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Aout', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
j = 0
for i in t2:
    t3.append(i)
    t3.append(t1[j])
    j += 1
print(t3)
