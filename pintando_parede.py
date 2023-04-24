# Faça um programa que leia a largura e a altura 
# de uma parede em metros, calcule a sua área e 
# a quantidade de tinta necessária para pintá-la, 
# sabendo que cada litro de tinta pinta uma área de 2m²

altura = int(input("Digite sua altura em metros \n"))
largura = int(input("Digite sua largura \n"))
area = altura*largura
litro = area/2

print("Sua dimensão é {}x{}".format(altura, largura))
print("Sua área é {}. Portanto você precisará de {} litros de tinta".format(area,litro))
