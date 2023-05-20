salario = float(input("qual seu salario?? -> "))

if salario <= 2000.00:
  print("vc está insento congrations")
  cleiton = input("tem mais algum desconto manda ae? sim ou não ->")
  cleiton == "sim"
  salario2 = float(input("quanto q é? "))
  print(salario - salario2)
  #elif == "não":
  # print("oi")

elif salario >= 2000.01 and salario <= 3000.00:
  print("O DESCONTO SERÁ DE 8%")
  desconto = salario * 0.08
  print("seu desconte será de ", desconto)
  salarioliquiado = salario - desconto
  print("SEU SALARIO SERÁ DE -> ", salarioliquiado)
  cleiton = input("tem mais algum desconto manda ae? sim ou não ->")
  if cleiton == "sim":
    desconto2 = float(input("quanto que é? -> "))
    print("seu money no final so sobro -> ", salarioliquiado - desconto2)
  else:
    print("então te sobrou - > ", salarioliquiado)

elif salario >= 3000.01 and salario <= 4500.00:
  print("O DESCONTO SERÁ DE 18%")
  desconto = salario * 0.18
  print("seu desconte será de ", desconto)
  salarioliquiado = salario - desconto
  print("SEU SALARIO SERÁ DE -> ", salarioliquiado)
  cleiton = input("tem mais algum desconto manda ae? sim ou não ->")
  if cleiton == "sim":
    desconto2 = float(input("quanto que é? -> "))
    print("seu money no final so sobro -> ", salarioliquiado - desconto2)
  else:
    print("então te sobrou - > ", salarioliquiado)

elif salario >= 4500.01:
  print("O DESCONTO SERÁ DE 28%")
  desconto = salario * 0.28
  print("seu desconte será de ", desconto)
  salarioliquiado = salario - desconto
  print("SEU SALARIO SERÁ DE -> ", salarioliquiado)
  cleiton = input("tem mais algum desconto manda ae? sim ou não ->")
  if cleiton == "sim":
    desconto2 = float(input("quanto que é? -> "))
    print("seu money no final so sobro -> ", salarioliquiado - desconto2)
  else:
    print("então te sobrou - > ", salarioliquiado)