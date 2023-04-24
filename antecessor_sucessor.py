# Faça um script que leia um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor:

num1 = int(input("Digite um número: \n"))
print("o antecessor de {} é: {}".format(num1, num1 - 1))
print("O sucessor de {} é: {}".format(num1, num1 + 1))