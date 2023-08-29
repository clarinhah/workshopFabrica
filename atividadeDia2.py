
nome = input("Digite seu nome:")
idade = input("Digite sua idade")

maiorIdade = 18

try:
   if int(idade) >=  maiorIdade:
    print("Parabéns Senhor(a)",nome , "você está apto(a) para tirar sua carteira")
   else:
    print("Desculpe senhor(a)", nome , "você ainda não está apto(a) para tirar sua carteira")
except ValueError:
   raise ValueError("Digite o valor do número válido")


