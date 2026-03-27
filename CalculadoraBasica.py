print("***************************")
print("*    CALCULADORA BÁSICA   *")
print("***************************")
print("* Escolha uma operação:   *")
print("* 1 - Soma (+)            *")
print("* 2 - Subtração (-)       *")
print("* 3 - Multiplicação (*)   *")
print("* 4 - Divisão (/)         *")
print("***************************")

op = int(input("\nDigite a opção: "))

n1 = float(input("\nDigite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

if op == 1:
    resultado = n1 + n2
    print("\nResultado:", resultado)

elif op == 2:
    resultado = n1 - n2
    print("\nResultado:", resultado)

elif op == 3:
    resultado = n1 * n2
    print("\nResultado:", resultado)

elif op == 4:
    resultado = n1 / n2
    print("\nResultado:", resultado)

else:
    print("\nOpção inválida!")

print("\n***************************")
print("*     FIM DO PROGRAMA     *")
print("***************************")