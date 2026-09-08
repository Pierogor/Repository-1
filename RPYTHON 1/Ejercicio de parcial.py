num = int(input("numero a evaluar"))
cont = 0

for i in range(1,num+1,1):
    if (num %i) == 0:
        cont += 1

if cont == 0: 
    print(f"{num} es primo!")
else: 
    print(f"{num} no es primo")