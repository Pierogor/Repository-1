

num1 = float(input("Numero 1>>"))
oper = input()
num2 = float(input("Numero2>>"))

if oper == "+":
    resul = num1 + num2
elif oper == "-":
    resul = num1 - num2
elif oper == "*":
    resul = num1 * num2
elif oper == "/":
    resul= num1 / num2
elif oper == "^":
    resul = num1 **num2
else: 
    print("Operacion invalida bruto")
    resul= "No ejecutado" 

print(f"{num1}{oper}{num2} = {resul}")
    
