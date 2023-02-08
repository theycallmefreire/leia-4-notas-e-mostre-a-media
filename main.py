#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
n = []  
for i in range(4):
  notas = int(input("diga-me uma nota:"))
  n.append(notas)

media = (n[0] +n[1] + n[2] +n[3])/4
print('a media dos alunos é:',media)