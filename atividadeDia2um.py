multa = 7
velocidade = 80


vel = int(input("Qual a velocidade estimada você dirigiu?"))

punicao = int(multa * vel)

if vel>= velocidade:
    print("Você excedeu o limite e irá pagar:", punicao)
else:
 print("Você não excedeu o limite, não existe multa")
   



