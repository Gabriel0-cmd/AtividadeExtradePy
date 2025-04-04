import random


def obter_numero():
  numero = random.randint(1, 100)
  return numero

def advinhar_resultado(numero, usuario):
  if usuario > numero:
    print("O número é menor. Tente novamente")
  elif usuario < numero:
    print("O número é maior. Tente novamente")
  else:
    print("Parabéns você acertou!!")


def monitorar():
  numero = obter_numero()
  while True:
    usuario = float(input("Digite um número: "))
    advinhar_resultado(numero, usuario)

monitorar()