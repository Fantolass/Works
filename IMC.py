altura = float(input("Informe sua altura: "))
peso = float(input("Informe seu peso: "))
c = peso / altura**2
print("   ")
print("Seu índice de massa corporal é igual a:", c)
print("   ")
if (c < 18.6):
  print("Abaixo do normal")
elif(18.6 <= c <= 24.9):
  print("Normal")
elif(25 >= c >= 29.9):
  print("Sobrepeso")
elif(30 >= c >= 34.9):
  print("Obesidade grau I")
elif(35 >= c >= 39.9):
  print("Obesidade grau II")
elif(c > 40):
  print("Obesidade grau III")